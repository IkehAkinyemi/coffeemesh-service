from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, conlist, conint

class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'

class Status(Enum):
    created = 'created'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'

quantity_type = conint(ge=1, strict=True)

class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[quantity_type] = 1

create_order_type = conlist(OrderItemSchema, min_items=1)

class CreateOrderSchema(BaseModel):
    order: create_order_type

class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: Status

class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]