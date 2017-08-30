# -*- coding:UTF-8 -*-

users = {
"Angelica":{"Blue Traveler":3.5,"Broken Bells":2.0,
"Norah Jones":4.5,"Phoenix":5.0,"Slightly Stoopid":1.5,
"The Strokes":2.5,"Vampire Weekend":2.0},

"Bill":{"Blue Traveler":2.0,"Broken Bells":3.5,
"Deadmau5":4.0,"Phoenix":2.0,"Slightly Stoopid":3.5,
"Vampire Weekend":3.0},

"Chan":{"Blue Traveler":5.0,"Broken Bells":1.0,
"Deadmau5":1.0,"Norah Jones":3.0,"Phoenix":5.0,
"Slightly Stoopid":1.0},

"Dan":{"Blue Traveler":3.0,"Broken Bells":4.0,
"Deadmau5":4.5,"Phoenix":3.0,"Slightly Stoopid":4.5,
"The Strokes":4.0,"Vampire Weekend":2.0},

"Hailey":{"Broken Bells":4.0,"Deadmau5":1.0,
"Norah Jones":4.0,"The Strokes":4.0,"Vampire Weekend":1.0},

"Jordyn":{"Broken Bells":4.5,"Deadmau5":4.0,
"Norah Jones":5.0,"Phoenix":5.0,"Slightly Stoopid":4.5,
"The Strokes":4.0,"Vampire Weekend":4.0},

"Sam":{"Blue Traveler":5.0,"Broken Bells":2.0,
"Norah Jones":3.0,"Phoenix":5.0,"Slightly Stoopid":4.0,
"The Strokes":5.0},

"Veronica":{"Blue Traveler":3.0,"Norah Jones":5.0,
"Phoenix":4.0,"Slightly Stoopid":2.5,
"The Strokes":3.0},

}

users2 = {"Amy":{"Taylor Swift":4,"PSY":3,"Whitney Houston":4},
		  "Ben":{"Taylor Swift":5,"PSY":2},
		  "Clara":{"PSY":3.5,"Whitney Houston":4},
		  "Daisy":{"Taylor Swift":5,"Whitney Houston":3}}

users3 = {"David":{"Imagine Dragons":3,"Daft Punk":5,
					"Lorde":4,"Fall Out Boy":1},
		  "Matt":{"Imagine Dragons":3,"Daft Punk":4,
		            "Lorde":4,"Fall Out Boy":1},
		  "Ben":{"Kacey Musgraves":4,"Imagine Dragons":3,
		          "Lorde":3,"Fall Out Boy":1},
		  "Chris":{"Kacey Musgraves":4,"Imagine Dragons":4,
		            "Daft Punk":4,"Lorde":3,"Fall Out Boy":1},
	      "Tori":{"Kacey Musgraves":5,"Imagine Dragons":4,
		            "Daft Punk":5,"Fall Out Boy":3}
}

# users3的物品列表
content = ["Imagine Dragons","Daft Punk","Fall Out Boy","Lorde","Kacey Musgraves"]

def loadMovieLens(filename):
    data = {}
    i = 0
    f = open(filename)
    for line in f:
		print ''
		i += 1
		fields = line.strip().split(',')
		userIDs = int(fields[0])
		movieIDs = int(fields[1])
		ratings = float(fields[2])
		#print userIDs
		data.setdefault(i,{})
		data[i].setdefault('userID',userIDs)
		data[i].setdefault('movieID',movieIDs)
		data[i].setdefault('rating',ratings)
    return data
