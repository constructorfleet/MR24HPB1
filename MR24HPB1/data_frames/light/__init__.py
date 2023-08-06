import dataclasses
from typing import Dict, Any

from construct import Const, Int8ub, Select, Aligned
from construct_typed import DataclassMixin, csfield, DataclassStruct
@dataclasses.dataclass
class RGB(DataclassMixin):
    red: int = csfield(Int8ub)
    green: int = csfield(Int8ub)
    blue: int = csfield(Int8ub)

@dataclasses.dataclass
class DIYMode(DataclassMixin):
    _diy: int = csfield(Const(b"\x0a"))
    diy_sene: int = csfield(Int8ub)


@dataclasses.dataclass
class SceneMode(DataclassMixin):
    _scene: int = csfield(Const(b"\x04"))
    scene: int = csfield(Int8ub)


@dataclasses.dataclass
class RhythmMusic(DataclassMixin):
    rhythm: int = csfield(Const(b"\x04"))


@dataclasses.dataclass
class RollingMusic(DataclassMixin):
    rolling: int = csfield(Const(b"\x03"))
    start_color: Dict = csfield(DataclassStruct(RGB))
    end_color: Dict = csfield(DataclassStruct(RGB))


@dataclasses.dataclass
class SpectrumMusic(DataclassMixin):
    spectrum: int = csfield(Const(b"\x01"))
    start_color: Dict = csfield(DataclassStruct(RGB))
    end_color: Dict = csfield(DataclassStruct(RGB))


@dataclasses.dataclass
class EnergeticMusic(DataclassMixin):
    energetic: int = csfield(Const(b"\x00"))


@dataclasses.dataclass
class MusicMode(DataclassMixin):
    _music: int = csfield(Const(b"\x01"))
    music_mode: Any = csfield(
        Select(
            DataclassStruct(EnergeticMusic),
            DataclassStruct(SpectrumMusic),
            DataclassStruct(RollingMusic),
            DataclassStruct(RhythmMusic)))


@dataclasses.dataclass
class ColorMode(DataclassMixin):
    _manual: int = csfield(Const(b"\x02"))
    rgb_color: Dict = csfield(DataclassStruct(RGB))
    use_kelvin: bool = csfield(Int8ub)
    kelvin_color: Dict = csfield(DataclassStruct(RGB))


@dataclasses.dataclass
class Mode(DataclassMixin):
    _mode: int = csfield(Const(b"\x05"))
    mode: Dict = csfield(
        Select(
            DataclassStruct(ColorMode),
            DataclassStruct(MusicMode),
            DataclassStruct(SceneMode)))


@dataclasses.dataclass
class Brightness(DataclassMixin):
    _brightness: int = csfield(Const(b"\x04"))
    brightness: bool = csfield(Int8ub)


@dataclasses.dataclass
class Active(DataclassMixin):
    _active_state: int = csfield(Const(b"\x01"))
    is_active: bool = csfield(Int8ub)


@dataclasses.dataclass
class LightReport(DataclassMixin):
    report: int = csfield(Const(b"\xAA"))
    state: Any = csfield(Aligned(18,
        Select(DataclassStruct(Active),
               DataclassStruct(Brightness),
               DataclassStruct(Mode))))
