from typing import TYPE_CHECKING
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import func
if TYPE_CHECKING:
    from .product import Product
    from.order_product_association import OrderProductAssociation


class Order(Base):
    promocode: Mapped[str | None]
    create_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
    # products: Mapped[list["Product"]] = relationship(
    #     secondary="order_product_association",
    #     back_populates="orders"
    # )

    products_details: Mapped[list["OrderProductAssociation"]] = relationship(
        back_populates="order"
    )