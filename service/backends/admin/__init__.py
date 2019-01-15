# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from common.utils.imports import import_submodules
# import pkgutil
from django.contrib import admin
from restful.contrib.utils.imports import import_submodules


# def import_submodules(context, root_module, path):
#     """
#     Import all submodules and register them in the ``context`` namespace.
#
#     >>> import_submodules(locals(), __name__, __path__)
#     """
#     for loader, module_name, is_pkg in pkgutil.walk_packages(path, root_module + '.'):
#         module = loader.find_module(module_name).load_module(module_name)
#         for k, v in vars(module).iteritems():
#             if not k.startswith('_'):
#                 context[k] = v
#         context[module_name] = module


class ReadonlyModelAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        opts = self.opts
        view_permission = 'view_%s' % self.model._meta.module_name
        return request.user.has_perm(opts.app_label + '.' + view_permission)

    def has_change_permission(self, request, obj=None):
        if hasattr(self, 'has_change'):
            if self.has_change:
                return True

        return super(ReadonlyModelAdmin, self).has_change_permission(request, obj)

    def get_model_perms(self, request):
        value = super(ReadonlyModelAdmin, self).get_model_perms(request)
        value['view'] = self.has_view_permission(request)

        return value

    def changelist_view(self, request, extra_context=None):
        if self.has_view_permission(request, None):
            self.has_change = True

        result = super(ReadonlyModelAdmin, self).changelist_view(request, extra_context)
        self.has_change = False
        return result


import_submodules(locals(), __name__, __path__)
