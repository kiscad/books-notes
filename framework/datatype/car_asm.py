from dataclasses import dataclass, field
from typing import List

from .door import Door
from .headlight import HeadLight
from .ipart import IPart
from .rearlight import RearLight
from .sideview_mirror import SideviewMirror
from .wheel import Wheel
from .windshield import WindShield


@dataclass
class CarAsm:
    headlight_r: HeadLight = field(default_factory=HeadLight)
    headlight_l: HeadLight = field(default_factory=HeadLight)
    windshield_f: WindShield = field(default_factory=WindShield)
    windshield_b: WindShield = field(default_factory=WindShield)
    wheel_fr: Wheel = field(default_factory=Wheel)
    wheel_fl: Wheel = field(default_factory=Wheel)
    wheel_br: Wheel = field(default_factory=Wheel)
    wheel_bl: Wheel = field(default_factory=Wheel)
    door_fr: Door = field(default_factory=Door)
    door_fl: Door = field(default_factory=Door)
    door_br: Door = field(default_factory=Door)
    door_bl: Door = field(default_factory=Door)
    rearlight_r: RearLight = field(default_factory=RearLight)
    rearlight_l: RearLight = field(default_factory=RearLight)
    sidemirror_r: SideviewMirror = field(default_factory=SideviewMirror)
    sidemirror_l: SideviewMirror = field(default_factory=SideviewMirror)

    def list_parts(self) -> List[IPart]:
        return [self.door_bl, self.door_br]
