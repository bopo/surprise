# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# import six
# from django.http import Http404, JsonResponse
# from django.shortcuts import redirect
# from django.utils import log
# from django_extensions.utils.validatingtemplatetags import errors
# from rest_framework import exceptions, status
# from rest_framework.compat import set_rollback
# from rest_framework.exceptions import PermissionDenied
# from rest_framework.response import Response
#
#
# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code
#
#     return response
#
#
# def exception_handler(exc, context):
#     """
#     Returns the response that should be used for any given exception.
#
#     By default we handle the REST framework `APIException`, and also
#     Django's built-in `Http404` and `PermissionDenied` exceptions.
#
#     Any unhandled exceptions may return `None`, which will cause a 500 error
#     to be raised.
#     """
#     if isinstance(exc, exceptions.APIException):
#         headers = {}
#         if getattr(exc, 'auth_header', None):
#             headers['WWW-Authenticate'] = exc.auth_header
#         if getattr(exc, 'wait', None):
#             headers['Retry-After'] = '%d' % exc.wait
#
#         if isinstance(exc.detail, (list, dict)):
#             data = exc.detail
#         else:
#             data = {'detail': exc.detail}
#
#         set_rollback()
#         return Response(data, status=exc.status_code, headers=headers)
#     elif isinstance(exc, Http404):
#         msg = _('Not found.')
#         data = {'detail': six.text_type(msg)}
#
#         set_rollback()
#         return Response(data, status=status.HTTP_404_NOT_FOUND)
#
#     elif isinstance(exc, PermissionDenied):
#         msg = _('Permission denied.')
#         data = {'detail': six.text_type(msg)}
#
#         set_rollback()
#         return Response(data, status=status.HTTP_403_FORBIDDEN)
#
#     # Note: Unhandled exceptions will raise a 500 error.
#     return None
#
#
# class Error(Exception):
#     def __init__(self, err_code, err_message='Internal Server Error',
#             message=u'服务器异常', status_code=status.HTTP_400_BAD_REQUEST):
#         self.err_code = err_code
#         self.err_message = err_message
#         self.message = message
#         self.status_code = status_code
#
#     def __unicode__(self):
#         return u'[Error] %d: %s(%d)' % (self.err_code, self.err_message, self.status_code)
#
#     def getResponse(self):
#         return ErrorResponse(self.err_code, self.err_message, self.message, self.status_code)
#
#
# def ErrorResponse(err_code=errors.SYSTEM_ERROR, err_message='Internal Server Error',
#         message=u'服务器异常', status=status.HTTP_400_BAD_REQUEST, headers=None):
#     err = {
#         'error_code': err_code,
#         'error': err_message,
#         'message': message,
#     }
#     return Response(err, status, headers=headers)
#
#
# class ForeignObjectRelDeleteError(object):
#     pass
#
#
# class ModelDontHaveIsActiveFiled(object):
#     pass
#
#
# class RestPermissionDenied(object):
#     pass
#
#
# def custom_exception_handler(exc, context):
#     if isinstance(exc, Error):
#         set_rollback()
#         return ErrorResponse(exc.err_code, exc.err_message, exc.message, status=exc.status_code)
#
#     if isinstance(exc, (ForeignObjectRelDeleteError, ModelDontHaveIsActiveFiled)):
#         set_rollback()
#         return ErrorResponse(errors.PermissionDenied, unicode(exc), u'抱歉, 已有其他数据与之关联, 禁止删除',
#             status=status.HTTP_403_FORBIDDEN)
#
#     if isinstance(exc, (RestPermissionDenied, PermissionDenied)):
#         msg = _('Permission denied.')
#         data = {
#             'detail': six.text_type(msg)
#         }
#         exc_message = str(exc)
#         if 'CSRF' in exc_message:
#             data['detail'] = exc_message
#
#         set_rollback()
#
#         return ErrorResponse(errors.PermissionDenied, data, u'opps, 您没有对应的权限', status=status.HTTP_403_FORBIDDEN)
#
#     log.error(exc)
#
#     return ErrorResponse(errors.SYSTEM_ERROR, 'Internal Server Error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#
# def render_500(request):
#     if request.is_ajax():
#         err = {
#             'error_code': errors.SYSTEM_ERROR,
#             'error': 'Internal Server Error',
#             'message': 'Internal Server Error',
#         }
#         return JsonResponse(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     return redirect('/error/?c=500')
