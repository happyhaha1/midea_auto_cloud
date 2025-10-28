from homeassistant.const import Platform, UnitOfTemperature, UnitOfTime, PERCENTAGE
from homeassistant.components.sensor import SensorStateClass, SensorDeviceClass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass

DEVICE_MAPPING = {
    "default": {
        "rationale": ["off", "on"],
        "queries": [{}],
        "centralized": [
            "power", "swing", "display_on_off", "temp_wind_switch",
        ],
        "entities": {
            Platform.SWITCH: {
                "display_on_off": {
                    "device_class": SwitchDeviceClass.SWITCH,
                    "rationale": ["on", "off"]
                },
                "temp_wind_switch": {
                    "device_class": SwitchDeviceClass.SWITCH,
                },
            },
            Platform.FAN: {
                "fan": {
                    "power": "power",
                    "speeds": [
                        {"gear": "1"},
                        {"gear": "2"},
                        {"gear": "3"},
                        {"gear": "4"},
                        {"gear": "5"},
                        {"gear": "6"},
                        {"gear": "7"},
                        {"gear": "8"},
                        {"gear": "9"},
                    ],
                    "oscillate": "swing",
                    "preset_modes": {
                        "normal": {"mode": "normal"},
                        "sleep": {"mode": "sleep"},
                        "baby": {"mode": "baby"}
                    }
                }
            },
            Platform.SELECT: {
                "voice": {
                    "options": {
                        "open_buzzer": {"voice": "open_buzzer"},
                        "close_buzzer": {"voice": "close_buzzer"},
                        "mute": {"voice": "mute"}
                    }
                },
                "swing_angle": {
                    "options": {
                        "unknown": {"swing_angle": "unknown"},
                        "30": {"swing_angle": "30"},
                        "60": {"swing_angle": "60"},
                        "90": {"swing_angle": "90"},
                        "120": {"swing_angle": "120"},
                        "150": {"swing_angle": "150"},
                        "180": {"swing_angle": "180"}
                    }
                },
                "swing_direction": {
                    "options": {
                        "unknown": {"swing_direction": "unknown"},
                        "horizontal": {"swing_direction": "horizontal"},
                        "vertical": {"swing_direction": "vertical"},
                        "both": {"swing_direction": "both"}
                    }
                },
                "sleep_sensor": {
                    "options": {
                        "none": {"sleep_sensor": "none"},
                        "light": {"sleep_sensor": "light"},
                        "sound": {"sleep_sensor": "sound"},
                        "both": {"sleep_sensor": "both"}
                    }
                },
            },
            Platform.SENSOR: {
                "real_gear": {
                    "device_class": SensorDeviceClass.ENUM,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "dust_life_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.HOURS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "filter_life_time": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.HOURS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "temperature_feedback": {
                    "device_class": SensorDeviceClass.TEMPERATURE,
                    "unit_of_measurement": UnitOfTemperature.CELSIUS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "water_feedback": {
                    "device_class": SensorDeviceClass.ENUM,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "timer_off_hour": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.HOURS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "timer_off_minute": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "timer_on_hour": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.HOURS,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "timer_on_minute": {
                    "device_class": SensorDeviceClass.DURATION,
                    "unit_of_measurement": UnitOfTime.MINUTES,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "pm25": {
                    "device_class": SensorDeviceClass.PM25,
                    "unit_of_measurement": "µg/m³",
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "ud_swing_angle": {
                    "device_class": SensorDeviceClass.ENUM,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "lr_diy_down_percent": {
                    "device_class": SensorDeviceClass.BATTERY,
                    "unit_of_measurement": PERCENTAGE,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "lr_diy_up_percent": {
                    "device_class": SensorDeviceClass.BATTERY,
                    "unit_of_measurement": PERCENTAGE,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "ud_diy_down_percent": {
                    "device_class": SensorDeviceClass.BATTERY,
                    "unit_of_measurement": PERCENTAGE,
                    "state_class": SensorStateClass.MEASUREMENT
                },
                "ud_diy_up_percent": {
                    "device_class": SensorDeviceClass.BATTERY,
                    "unit_of_measurement": PERCENTAGE,
                    "state_class": SensorStateClass.MEASUREMENT
                }
            }
        }
    }
}
