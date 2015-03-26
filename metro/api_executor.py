#
#    (c) 2014 Morning Project Samurai
#
#    This file is part of Burasabori.
#    Burasabori is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    Burasabori is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'Junya Kaneko'

from contrib.api_executor.api_executor import ApiExecutor

METRO_KEY = 'be36f224acbc1eb0d5dba250352a91766a738fbaf175c11039cfe32354a17d4f'

class MetroApiExecutor(ApiExecutor):
    def __init__(self, parameters):
        base_url = 'https://api.tokyometroapp.jp/api/v2/datapoints'
        parameters = parameters
        super(MetroApiExecutor, self).__init__(base_url, parameters)