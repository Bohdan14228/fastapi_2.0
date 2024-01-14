from typing import TYPE_CHECKING
from .base import Base
from sqlalchemy.orm import Mapped, relationship
if TYPE_CHECKING:
    from .order import OrderProductAssociation
    from .order import Order


class Product(Base):
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[str]

    orders: Mapped[list["Order"]] = relationship(
        secondary="order_product_association",
        back_populates="products"
    )

    orders_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="product",
    )
