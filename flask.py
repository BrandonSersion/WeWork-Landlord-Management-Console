from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def rooms():
  s = [{
  "roomId": "1",
  "floor": "",
  "squareFootage": "",
  "occupant": "",
  "rent": "",
  "leaseEndDate": ""
  },{
  "roomId": "2",
  "floor": "9",
  "squareFootage": "1139",
  "occupant": "Michael Norman",
  "rent": "511.91",
  "leaseEndDate": "1973-01-25"
  },{
  "roomId": "3",
  "floor": "5",
  "squareFootage": "1452",
  "occupant": "James Cook",
  "rent": "618.97",
  "leaseEndDate": "1971-11-04"
  },{
  "roomId": "4",
  "floor": "11",
  "squareFootage": "494",
  "occupant": "Timothy Moore",
  "rent": "472.21",
  "leaseEndDate": "1994-06-23"
  },{
  "roomId": "5",
  "floor": "4",
  "squareFootage": "662",
  "occupant": "Mary Blake",
  "rent": "829.05",
  "leaseEndDate": "1971-08-16"
  },{
  "roomId": "6",
  "floor": "1",
  "squareFootage": "1421",
  "occupant": "David Thompson",
  "rent": "1494.4",
  "leaseEndDate": "1997-08-11"
  },{
  "roomId": "7",
  "floor": "8",
  "squareFootage": "1014",
  "occupant": "Jeffery Rogers",
  "rent": "303.91",
  "leaseEndDate": "1973-10-25"
  },{
  "roomId": "8",
  "floor": "9",
  "squareFootage": "1484",
  "occupant": "Mariah Johnston",
  "rent": "837.07",
  "leaseEndDate": "1978-03-24"
  },{
  "roomId": "9",
  "floor": "11",
  "squareFootage": "1359",
  "occupant": "Juan Webster",
  "rent": "728.32",
  "leaseEndDate": "1970-12-12"
  },{
  "roomId": "10",
  "floor": "4",
  "squareFootage": "462",
  "occupant": "Derrick Davis",
  "rent": "1314.46",
  "leaseEndDate": "1997-09-21"
  },{
  "roomId": "11",
  "floor": "2",
  "squareFootage": "1009",
  "occupant": "Nichole Brown",
  "rent": "544.9",
  "leaseEndDate": "1971-04-19"
  },{
  "roomId": "12",
  "floor": "7",
  "squareFootage": "773",
  "occupant": "Nicholas Terry",
  "rent": "609.64",
  "leaseEndDate": "1984-06-21"
  },{
  "roomId": "13",
  "floor": "11",
  "squareFootage": "948",
  "occupant": "Richard Proctor",
  "rent": "390.44",
  "leaseEndDate": "1990-03-13"
  },{
  "roomId": "14",
  "floor": "11",
  "squareFootage": "945",
  "occupant": "Rachel Koch",
  "rent": "651.88",
  "leaseEndDate": "1971-08-04"
  },{
  "roomId": "15",
  "floor": "9",
  "squareFootage": "1056",
  "occupant": "Jonathan Cochran",
  "rent": "1456.64",
  "leaseEndDate": "2004-03-24"
  },{
  "roomId": "16",
  "floor": "11",
  "squareFootage": "423",
  "occupant": "Amber Rodriguez",
  "rent": "1294.5",
  "leaseEndDate": "1992-12-17"
  },{
  "roomId": "17",
  "floor": "3",
  "squareFootage": "1479",
  "occupant": "Brian Castro",
  "rent": "537.94",
  "leaseEndDate": "1971-12-03"
  },{
  "roomId": "18",
  "floor": "10",
  "squareFootage": "978",
  "occupant": "Jennifer Roberts",
  "rent": "1107.77",
  "leaseEndDate": "2000-03-28"
  },{
  "roomId": "19",
  "floor": "11",
  "squareFootage": "561",
  "occupant": "Jay Bryant",
  "rent": "1366.46",
  "leaseEndDate": "2014-03-10"
  },{
  "roomId": "20",
  "floor": "7",
  "squareFootage": "464",
  "occupant": "Mathew Scott",
  "rent": "726.13",
  "leaseEndDate": "2011-12-01"
  },{
  "roomId": "21",
  "floor": "9",
  "squareFootage": "1060",
  "occupant": "Eric Thompson",
  "rent": "515.51",
  "leaseEndDate": "1973-06-14"
  },{
  "roomId": "22",
  "floor": "6",
  "squareFootage": "1375",
  "occupant": "Theresa Phillips",
  "rent": "1116.34",
  "leaseEndDate": "2008-06-01"
  },{
  "roomId": "23",
  "floor": "6",
  "squareFootage": "996",
  "occupant": "John Lowe",
  "rent": "925.19",
  "leaseEndDate": "2017-08-06"
  },{
  "roomId": "24",
  "floor": "9",
  "squareFootage": "683",
  "occupant": "Christopher Frederick",
  "rent": "894.99",
  "leaseEndDate": "1978-10-27"
  },{
  "roomId": "25",
  "floor": "9",
  "squareFootage": "735",
  "occupant": "Timothy Lane",
  "rent": "605.7",
  "leaseEndDate": "1980-12-04"
  },{
  "roomId": "26",
  "floor": "2",
  "squareFootage": "1305",
  "occupant": "Rachel Gonzales",
  "rent": "1124.58",
  "leaseEndDate": "1989-02-18"
  },{
  "roomId": "27",
  "floor": "1",
  "squareFootage": "1278",
  "occupant": "Stephen Pitts",
  "rent": "871.31",
  "leaseEndDate": "2001-07-29"
  },{
  "roomId": "28",
  "floor": "4",
  "squareFootage": "1256",
  "occupant": "Richard Gonzales",
  "rent": "1331.79",
  "leaseEndDate": "1975-09-26"
  },{
  "roomId": "29",
  "floor": "2",
  "squareFootage": "1090",
  "occupant": "Darrell Paul",
  "rent": "1434.17",
  "leaseEndDate": "1995-06-04"
  },{
  "roomId": "30",
  "floor": "3",
  "squareFootage": "1133",
  "occupant": "April Jones",
  "rent": "526.96",
  "leaseEndDate": "1996-01-30"
  },{
  "roomId": "31",
  "floor": "2",
  "squareFootage": "1463",
  "occupant": "Susan Rogers",
  "rent": "436.99",
  "leaseEndDate": "1984-09-08"
  },{
  "roomId": "32",
  "floor": "12",
  "squareFootage": "988",
  "occupant": "Heather Evans",
  "rent": "542.88",
  "leaseEndDate": "1984-03-17"
  },{
  "roomId": "33",
  "floor": "5",
  "squareFootage": "830",
  "occupant": "Michael Johnson",
  "rent": "1019.27",
  "leaseEndDate": "2002-05-05"
  },{
  "roomId": "34",
  "floor": "3",
  "squareFootage": "969",
  "occupant": "Joseph Chandler",
  "rent": "982.19",
  "leaseEndDate": "1980-10-26"
  },{
  "roomId": "35",
  "floor": "1",
  "squareFootage": "873",
  "occupant": "Brandon Smith",
  "rent": "324.47",
  "leaseEndDate": "1981-02-19"
  },{
  "roomId": "36",
  "floor": "2",
  "squareFootage": "1039",
  "occupant": "Paul Mcclure",
  "rent": "1088.53",
  "leaseEndDate": "1999-07-14"
  },{
  "roomId": "37",
  "floor": "4",
  "squareFootage": "1178",
  "occupant": "Larry Cochran",
  "rent": "1111.02",
  "leaseEndDate": "1974-04-24"
  },{
  "roomId": "38",
  "floor": "10",
  "squareFootage": "1174",
  "occupant": "Rhonda Vargas",
  "rent": "1375.08",
  "leaseEndDate": "2014-03-12"
  },{
  "roomId": "39",
  "floor": "7",
  "squareFootage": "1285",
  "occupant": "Timothy Johnson",
  "rent": "1239.39",
  "leaseEndDate": "2000-04-11"
  },{
  "roomId": "40",
  "floor": "8",
  "squareFootage": "819",
  "occupant": "Dominique Parker",
  "rent": "428.64",
  "leaseEndDate": "1983-10-20"
  },{
  "roomId": "41",
  "floor": "4",
  "squareFootage": "1306",
  "occupant": "Mary Johnson",
  "rent": "1077.4",
  "leaseEndDate": "1985-10-31"
  },{
  "roomId": "42",
  "floor": "9",
  "squareFootage": "517",
  "occupant": "Lawrence Mcfarland",
  "rent": "903.53",
  "leaseEndDate": "1999-09-27"
  },{
  "roomId": "43",
  "floor": "1",
  "squareFootage": "940",
  "occupant": "Patrick Oconnell",
  "rent": "1257.72",
  "leaseEndDate": "2003-12-28"
  },{
  "roomId": "44",
  "floor": "4",
  "squareFootage": "792",
  "occupant": "Keith Johnson",
  "rent": "606.16",
  "leaseEndDate": "1977-09-30"
  },{
  "roomId": "45",
  "floor": "5",
  "squareFootage": "843",
  "occupant": "Joanna Rollins",
  "rent": "1344.22",
  "leaseEndDate": "1997-11-30"
  },{
  "roomId": "46",
  "floor": "10",
  "squareFootage": "811",
  "occupant": "Sydney Delgado",
  "rent": "728.3",
  "leaseEndDate": "1981-04-05"
  },{
  "roomId": "47",
  "floor": "8",
  "squareFootage": "1330",
  "occupant": "Wendy Myers",
  "rent": "596.02",
  "leaseEndDate": "2011-04-25"
  },{
  "roomId": "48",
  "floor": "5",
  "squareFootage": "545",
  "occupant": "James Clarke",
  "rent": "1436.23",
  "leaseEndDate": "2003-10-30"
  },{
  "roomId": "49",
  "floor": "3",
  "squareFootage": "1098",
  "occupant": "Jeremiah Walton",
  "rent": "324.22",
  "leaseEndDate": "1983-08-12"
  },{
  "roomId": "50",
  "floor": "4",
  "squareFootage": "1431",
  "occupant": "Dana Kerr",
  "rent": "1281.57",
  "leaseEndDate": "1976-07-02"
  },{
  "roomId": "51",
  "floor": "6",
  "squareFootage": "1444",
  "occupant": "Teresa Johnson",
  "rent": "629.42",
  "leaseEndDate": "1990-12-18"
  }]
  return jsonify(s)
