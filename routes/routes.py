from datetime import datetime

from fastapi import HTTPException, APIRouter
from tortoise.expressions import Q

from models import Dog
from models.order import Order
from schemas.order import OrderReadSchema, OrderCreateSchema

router = APIRouter(prefix='/orders')


@router.post("", response_model=OrderReadSchema, summary='Create order')
async def create_order(order: OrderCreateSchema):
    conflicting_order = await Order.filter(start_at=order.start_at)

    if len(conflicting_order) >= 2:
        raise HTTPException(status_code=400, detail="Both walkers are already booked for this time.")

    dog = await Dog.create(**order.dog.model_dump())

    return await Order.create(**order.model_dump(), pet_id=dog.id)


@router.get("/{date}", response_model=list[OrderReadSchema], summary='Get order list')
async def get_orders(date: str):
    selected_date = datetime.strptime(date, "%Y-%m-%d").date()
    start_datetime = datetime.combine(selected_date, datetime.min.time())
    end_datetime = datetime.combine(selected_date, datetime.max.time())

    selected_orders = await Order.filter(
        Q(start_at__gte=start_datetime) &
        Q(start_at__lte=end_datetime)
    )
    return selected_orders
