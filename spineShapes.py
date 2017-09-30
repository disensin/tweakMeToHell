
'''Shape format settings:
'shapeName': ([ 	(PPvalueX,PPvalueY,PPvalueZ),
					(PPvalueX,PPvalueY,PPvalueZ),
					(PPvalueX,PPvalueY,PPvalueZ),
					(PPvalueX,PPvalueY,PPvalueZ),
					(PPvalueX,PPvalueY,PPvalueZ),
					(PPvalueX,PPvalueY,PPvalueZ))
					],
				[valueKK],
				[valueDD]
)
'''


getShape = {
	'diamond': ([
					(-7, 0, 0), 
					(0, 0, 7),
					(7, 0, 0),
					(0, 0, -7),
					(-7, 0, 0),
					(0, 7, 0),
					(7, 0, 0),
					(0, -7, 0),
					(-7, 0, 0),
					(0, 0, 7),
					(0, 7, 0),
					(0, 0, -7),
					(0, -7, 0),
					(0, 0, 7)],
				[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
				1),
	}

