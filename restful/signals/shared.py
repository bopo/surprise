from restful.models.affairs import Affairs


def affairs(owner, price, rule):
    payment = round(float(price), 2)
    obj = Affairs.objects.create(owner=owner)
    obj.payment = payment
    obj.owner = owner
    obj.pay_type = 'in'
    obj.save()