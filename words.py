import urllib.request
import re
from datetime import *

def real_world_wordle_word(x=0):
	d0 = date(2021, 6, 19)
	d1 = date.today() + timedelta(x)
	x = (d1-d0).days % len(SOLUTIONS)
	return SOLUTIONS[x]

def get_solutions():
	raw = urllib.request.urlopen("https://www.nytimes.com/games/wordle/index.html")
	html_str = raw.read().decode("utf-8")
	raw.close()

	pattern = 'https://www.nytimes.com/games-assets/v2/wordle\.[A-Za-z0-9_-]*\.js'

	url = re.search(pattern, html_str).group(0)

	raw = urllib.request.urlopen(url)
	js_str = raw.read().decode("utf-8")
	raw.close()

	pattern = '\[[a-z\", ]{5,}\]'
	results = re.findall(pattern, js_str)

	s = results[0][1:-1]
	s = s.replace('"', '')
	s = s.split(',')

	o = results[1][1:-1]
	o = o.replace('"', '')
	o = o.split(',')

	return s,o

SOLUTIONS, OTHER = get_solutions()

WORDS = sorted(SOLUTIONS)

FEEDBACKS = ['00000', '00001', '00002', '00010', '00011',
			 '00012', '00020', '00021', '00022', '00100',
			 '00101', '00102', '00110', '00111', '00112',
			 '00120', '00121', '00122', '00200', '00201',
			 '00202', '00210', '00211', '00212', '00220',
			 '00221', '00222', '01000', '01001', '01002',
			 '01010', '01011', '01012', '01020', '01021',
			 '01022', '01100', '01101', '01102', '01110',
			 '01111', '01112', '01120', '01121', '01122',
			 '01200', '01201', '01202', '01210', '01211',
			 '01212', '01220', '01221', '01222', '02000',
			 '02001', '02002', '02010', '02011', '02012',
			 '02020', '02021', '02022', '02100', '02101',
			 '02102', '02110', '02111', '02112', '02120',
			 '02121', '02122', '02200', '02201', '02202',
			 '02210', '02211', '02212', '02220', '02221',
			 '02222', '10000', '10001', '10002', '10010',
			 '10011', '10012', '10020', '10021', '10022',
			 '10100', '10101', '10102', '10110', '10111',
			 '10112', '10120', '10121', '10122', '10200',
			 '10201', '10202', '10210', '10211', '10212',
			 '10220', '10221', '10222', '11000', '11001',
			 '11002', '11010', '11011', '11012', '11020',
			 '11021', '11022', '11100', '11101', '11102',
			 '11110', '11111', '11112', '11120', '11121',
			 '11122', '11200', '11201', '11202', '11210',
			 '11211', '11212', '11220', '11221', '11222',
			 '12000', '12001', '12002', '12010', '12011',
			 '12012', '12020', '12021', '12022', '12100',
			 '12101', '12102', '12110', '12111', '12112',
			 '12120', '12121', '12122', '12200', '12201',
			 '12202', '12210', '12211', '12212', '12220',
			 '12221', '20000', '20001', '20002', '20010',
			 '20011', '20012', '20020', '20021', '20022',
			 '20100', '20101', '20102', '20110', '20111',
			 '20112', '20120', '20121', '20122', '20200',
			 '20201', '20202', '20210', '20211', '20212',
			 '20220', '20221', '20222', '21000', '21001',
			 '21002', '21010', '21011', '21012', '21020',
			 '21021', '21022', '21100', '21101', '21102',
			 '21110', '21111', '21112', '21120', '21121',
			 '21122', '21200', '21201', '21202', '21210',
			 '21211', '21212', '21220', '21221', '22000',
			 '22001', '22002', '22010', '22011', '22012',
			 '22020', '22021', '22022', '22100', '22101',
			 '22102', '22110', '22111', '22112', '22120',
			 '22121', '22200', '22201', '22202', '22210',
			 '22211', '22220']#, '22222']


LETTER_COUNT = {'a': 975, 'b': 280, 'c': 475,
				'd': 393, 'e': 1230, 'f': 229,
				'g': 310, 'h': 387, 'i': 670,
				'j': 27, 'k': 210, 'l': 716,
				'm': 316, 'n': 573, 'o': 753,
				'p': 365, 'q': 29, 'r': 897,
				's': 668, 't': 729, 'u': 466,
				'v': 152, 'w': 194, 'x': 37,
				'y': 424, 'z': 40}

second_guesses = ['could', 'betel', 'cloth', 'spelt',
				  'floss', 'hotly', 'lipid', 'lingo',
				  'shout', 'islet', 'siege', 'empty',
				  'blunt', 'depth', 'plant', 'shied',
				  'forth', 'exist', 'noise', 'clout',
				  'cleat', 'black', 'chalk', 'knelt',
				  'slash', 'lefty', 'butch', 'until',
				  'email', 'image', 'slain', 'sepia',
				  'aisle', 'quasi', 'agony', 'alien',
				  'ankle', 'aside', 'amiss', 'notch',
				  'gulch', 'tonal', 'easel', 'slept',
				  'ample', 'claim', 'antic', 'adapt',
				  'naive', 'saint', 'daisy', 'count',
				  'outer', 'prong', 'sheep', 'perch',
				  'botch', 'grout', 'fiend', 'dirge',
				  'sprig', 'miser', 'first', 'plunk',
				  'draft', 'thump', 'shirk', 'skier',
				  'shire', 'aback', 'crowd', 'bleat',
				  'track', 'chant', 'champ', 'batch',
				  'arose', 'gland', 'aider', 'irate',
				  'stair', 'abled', 'afire', 'arise',
				  'tempo', 'satyr', 'safer', 'harsh',
				  'parse', 'nadir', 'chafe', 'outdo',
				  'rogue', 'rusty', 'rebus', 'roost',
				  'reuse', 'robin', 'caper', 'ridge',
				  'risky', 'resin', 'rinse', 'rhino',
				  'reign', 'royal', 'cabal', 'roast',
				  'rival', 'delay', 'carve', 'range',
				  'raspy', 'blond', 'rainy']