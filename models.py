from sqlmodel import SQLModel, Field, create_engine
from typing import Optional

class standings(SQLModel, table=True):
    Team: str = Field(primary_key=True)
    W: int | None = None
    L: int | None = None
    T: int | None = None
    PCT: float | None = None
    PF: int | None = None
    PA: int | None = None
    Net_Pts: int | None = None
    Home: str | None = None
    Away: str | None = None
    Div: str | None = None
    Div_Pct: float | None = None
    Conf: str | None = None
    Conf_Pct: float | None = None
    Non_Conf: str | None = None

class defense(SQLModel, table=True):
    Team: str = Field(primary_key=True)
    GP: int | None = None
    PA: int | None = None
    PA_G: float | None = None
    YDS_G: float | None = None
    PYDS: int | None = None
    PYDS_G: float | None = None
    RYDS: int | None = None
    RYDS_G: float | None = None
    SCK: int | None = None
    SCK_YDS: int | None = None
    DEF_INT: int | None = None
    INTTD: int | None = None
    FF: int | None = None
    FUMR: int | None = None
    FUMTD: int | None = None
    HUR: int | None = None
    PDEF: int | None = None
    SFTY: int | None = None


engine = create_engine("sqlite:///football.db")
SQLModel.metadata.create_all(engine)
