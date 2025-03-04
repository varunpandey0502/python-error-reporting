# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Client library for Error Reporting"""


from pkg_resources import get_distribution

# __version__ = get_distribution("google-cloud-error-reporting").version
__version__ = "1.4.1"

from google.cloud.error_reporting.client import Client
from google.cloud.error_reporting.client import HTTPContext
from google.cloud.error_reporting.util import build_flask_context

__all__ = ["__version__", "Client", "HTTPContext", "build_flask_context"]
