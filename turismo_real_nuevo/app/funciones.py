from .models import Carrito


def funcionCarrito(request):
    user = request.user if request.user.is_authenticated else None
    carro_id =request.session.get('carro_id')
    carro = Carrito.objects.filter(carro_id=carro_id).first()

      
    if carro is None:
        carro = Carrito.objects.create(user=user)

    if user and carro.user is None:
      carro.user = user
      carro.save()

    request.session['carro_id'] = carro.carro_id

    return carro