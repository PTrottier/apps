#os=Linux
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from github import releases

releases = [{
    'version': release['tag_name'].strip('v'),
    'released': release['published_at'][0:10]
} for release in releases('influxdata/influxdb') if not release['prerelease'] and release['tag_name'][0:2] == 'v2']
