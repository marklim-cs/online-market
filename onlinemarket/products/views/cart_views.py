from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from products.services import Cart

class CartView(APIView):
    def get(self, request):
        cart = Cart(request)
        return Response(
            {"data": list(cart.__iter__()),
            "total_price": cart.get_total_price()},
            status=status.HTTP_200_OK
            )

    def post(self, request, **kwargs):
        cart = Cart(request)

        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product=product)

        elif "clear" in request.data:
            cart.clear()

        else:
            product = request.data
            cart.add(
                product=product["product"],
                quantity=product["quantity"],
                override_quantity=product["overide_quantity"] if "overide_quantity" in product else False
            )

        return Response(
            {"message": "cart updated"},
            status=status.HTTP_202_ACCEPTED
                        )