from __future__ import annotations

import moderngl
import numpy as np

from manimlib.constants1 import GREY_C, YELLOW
from manimlib.constants1 import ORIGIN
from manimlib.mobject.types.point_cloud_mobject import PMobject
from manimlib.utils.iterables1 import resize_preserving_order

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy.typing as npt


DEFAULT_DOT_RADIUS = 0.05
DEFAULT_GLOW_DOT_RADIUS = 0.2
DEFAULT_GRID_HEIGHT = 6
DEFAULT_BUFF_RATIO = 0.5


class DotCloud(PMobject):
    CONFIG = {
        "color": GREY_C,
        "opacity": 1,
        "radius": DEFAULT_DOT_RADIUS,
        "glow_factor": 0,
        "shader_folder": "true_dot",
        "render_primitive": moderngl.POINTS,
        "shader_dtype": [
            ('point', np.float32, (3,)),
            ('radius', np.float32, (1,)),
            ('color', np.float32, (4,)),
        ],
    }

    def __init__(self, points: npt.ArrayLike = None, **kwargs):
        super().__init__(**kwargs)
        if points is not None:
            self.set_points(points)

    def init_data(self) -> None:
        super().init_data()
        self.data["radii"] = np.zeros((1, 1))
        self.set_radius(self.radius)

    def init_uniforms(self) -> None:
        super().init_uniforms()
        self.uniforms["glow_factor"] = self.glow_factor

    def to_grid(
        self,
        n_rows: int,
        n_cols: int,
        n_layers: int = 1,
        buff_ratio: float | None = None,
        h_buff_ratio: float = 1.0,
        v_buff_ratio: float = 1.0,
        d_buff_ratio: float = 1.0,
        height: float = DEFAULT_GRID_HEIGHT,
    ):
        n_points = n_rows * n_cols * n_layers
        points = np.repeat(range(n_points), 3, axis=0).reshape((n_points, 3))
        points[:, 0] = points[:, 0] % n_cols
        points[:, 1] = (points[:, 1] // n_cols) % n_rows
        points[:, 2] = points[:, 2] // (n_rows * n_cols)
        self.set_points(points.astype(float))

        if buff_ratio is not None:
            v_buff_ratio = buff_ratio
            h_buff_ratio = buff_ratio
            d_buff_ratio = buff_ratio

        radius = self.get_radius()
        ns = [n_cols, n_rows, n_layers]
        brs = [h_buff_ratio, v_buff_ratio, d_buff_ratio]
        self.set_radius(0)
        for n, br, dim in zip(ns, brs, range(3)):
            self.rescale_to_fit(2 * radius * (1 + br) * (n - 1), dim, stretch=True)
        self.set_radius(radius)
        if height is not None:
            self.set_height(height)
        self.center()
        return self

    def set_radii(self, radii: npt.ArrayLike):
        n_points = len(self.get_points())
        radii = np.array(radii).reshape((len(radii), 1))
        self.data["radii"] = resize_preserving_order(radii, n_points)
        self.refresh_bounding_box()
        return self

    def get_radii(self) -> np.ndarray:
        return self.data["radii"]

    def set_radius(self, radius: float):
        self.data["radii"][:] = radius
        self.refresh_bounding_box()
        return self

    def get_radius(self) -> float:
        return self.get_radii().max()

    def set_glow_factor(self, glow_factor: float) -> None:
        self.uniforms["glow_factor"] = glow_factor

    def get_glow_factor(self) -> float:
        return self.uniforms["glow_factor"]

    def compute_bounding_box(self) -> np.ndarray:
        bb = super().compute_bounding_box()
        radius = self.get_radius()
        bb[0] += np.full((3,), -radius)
        bb[2] += np.full((3,), radius)
        return bb

    def scale(
        self,
        scale_factor: float | npt.ArrayLike,
        scale_radii: bool = True,
        **kwargs
    ):
        super().scale(scale_factor, **kwargs)
        if scale_radii:
            self.set_radii(scale_factor * self.get_radii())
        return self

    def make_3d(self, reflectiveness: float = 0.5, shadow: float = 0.2):
        self.set_reflectiveness(reflectiveness)
        self.set_shadow(shadow)
        self.apply_depth_test()
        return self

    def get_shader_data(self) -> np.ndarray:
        shader_data = super().get_shader_data()
        self.read_data_to_shader(shader_data, "radius", "radii")
        self.read_data_to_shader(shader_data, "color", "rgbas")
        return shader_data


class TrueDot(DotCloud):
    def __init__(self, center: np.ndarray = ORIGIN, **kwargs):
        super().__init__(points=[center], **kwargs)


class GlowDots(DotCloud):
    CONFIG = {
        "glow_factor": 2,
        "radius": DEFAULT_GLOW_DOT_RADIUS,
        "color": YELLOW,
    }


class GlowDot(GlowDots, TrueDot):
    pass