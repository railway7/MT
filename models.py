from sqlalchemy import Column, String, Integer, DateTime, func, BigInteger, PickleType
from database import Base


class user(Base):
    __tablename__ = 'data'  # 数据表的表名

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(Integer, unique=True, nullable=False, comment='name')
    wm_latitude = Column(Integer, unique=False, nullable=False, comment='wm_latitude')
    wm_longitude = Column(Integer, unique=False, nullable=False, comment='wm_longitude')
    token = Column(PickleType, unique=False, nullable=False, comment='token')
    propId = Column(PickleType, unique=False, nullable=False, comment='propId')
    exchangeCoinNumber = Column(PickleType, unique=False, nullable=False, comment='exchangeCoinNumber')
    pushPlusToken = Column(PickleType, unique=False, nullable=False, comment='pushPlusToken')

    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='更新时间')

    __mapper_args__ = {"order_by": id}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f'{self.id}_{self.token}'