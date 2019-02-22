# Copyright 2017 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from . import wake_deflection
from . import wake_velocity


class Wake():
    """
    Wake is a container class for the various wake model objects. In particular,
    Wake holds references to the velocity and deflection models as well as their
    parameters.

    inputs:
        instance_dictionary: dict - the input dictionary;
            it should have the following key-value pairs:
                {
                    "description": str,

                    "properties": dict({

                        velocity_model: WakeVelocity

                        deflection_model: WakeDeflection

                        parameters: dict({

                            see WakeVelocity, WakeDeflection

                        })

                    }),

                }

    outputs:
        self: Wake - an instantiated Wake object
    """

    def __init__(self, instance_dictionary):

        self.description = instance_dictionary["description"]
        properties = instance_dictionary["properties"]
        parameters = properties["parameters"]

        self.velocity_models = {
            "jensen": wake_velocity.Jensen(parameters),
            "floris": wake_velocity.Floris(parameters),
            "gauss": wake_velocity.Gauss(parameters),
            "curl": wake_velocity.Curl(parameters)
        }
        self._velocity_model = self.velocity_models[properties["velocity_model"]]

        self.deflection_models = {
            "jimenez": wake_deflection.Jimenez(parameters),
            "gauss_deflection": wake_deflection.Gauss(parameters),
            "curl": wake_deflection.Curl(parameters)
        }
        self._deflection_model = self.deflection_models[properties["deflection_model"]]

    # Getters & Setters
    @property
    def deflection_function(self):
        return self.deflection_model.function

    @property
    def velocity_function(self):
        return self.velocity_model.function
