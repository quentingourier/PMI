import sys, os, sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen, QFont, QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 440, 720)
        self.setStyleSheet("background-color: #F7F7F6;")
        self.distance = 0

        # Add the label "MyPark"
        logo = QLabel()
        logo.setPixmap(QPixmap("logo.png").scaledToHeight(100))
        logo.setAlignment(Qt.AlignCenter)
        logo.setMinimumHeight(10)


        # Create the QWebEngineView widget to display the HTML file
        self.web_view = QWebEngineView()
        
        self.web_view.load(QUrl.fromLocalFile(os.path.abspath('mapme.html')))

        # button
        self.park_me_button = QPushButton("ParkMe")
        self.park_me_button.setStyleSheet("QPushButton{background-color: #385723; border-radius: 20px; color: white; font-size: 15px;}"
                           "QPushButton:hover{background-color: #006400;}")
        self.park_me_button.setFixedHeight(70)
        self.park_me_button.clicked.connect(self.show_route)

        #nav toolbar
        navigation_toolbar = QHBoxLayout()
        
        # Create the icons and add them to the navigation toolbar
        icon1 = QLabel()
        icon1.setPixmap(QPixmap("home.png").scaled(30,30))
        navigation_toolbar.addWidget(icon1)
        
        navigation_toolbar.addStretch(1)

        icon2 = QLabel()
        icon2.setPixmap(QPixmap("fav.png").scaled(30,30))
        navigation_toolbar.addWidget(icon2)

        navigation_toolbar.addStretch(1)
        
        icon3 = QLabel()
        icon3.setPixmap(QPixmap("report.png").scaled(30,30))
        navigation_toolbar.addWidget(icon3)

        navigation_toolbar.addStretch(1)
        
        icon4 = QLabel()
        icon4.setPixmap(QPixmap("settings.png").scaled(30,30))
        navigation_toolbar.addWidget(icon4)
        
    
        # Create the horizontal layout for the buttons
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.park_me_button)

        # Create the vertical layout for the web view and buttons
        v_layout = QVBoxLayout()
        # Add the navigation toolbar to the main layout
        v_layout.addWidget(logo)
        v_layout.addWidget(self.web_view)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(navigation_toolbar)

        # Set the central widget to contain the vertical layout
        central_widget = QWidget()
        central_widget.setLayout(v_layout)
        self.setCentralWidget(central_widget)

    def dist(self, coord1, coord2):
            from math import sin, cos, sqrt, atan2, radians
            R = 6373.0
            lat1 = radians(coord1[0])
            lon1 = radians(coord1[1])
            lat2 = radians(coord2[0])
            lon2 = radians(coord2[1])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            self.distance = R * c
            return self.distance
    
    def show_route(self):

        conn = sqlite3.connect("test_demo.db")
        cursor = conn.cursor()

        query = "SELECT coords FROM places WHERE status=0"
        cursor.execute(query)
        lot_dispo = cursor.fetchall()
        new_lot_dispo, lot_dispo2 = [], []
        for i in range(len(lot_dispo)):
            new_lot_dispo.append(list(lot_dispo[i]))
        for i in range(len(new_lot_dispo)):
            lot_dispo2.append([round(float(new_lot_dispo[i][0].split(',')[0]), 6), round(float(new_lot_dispo[i][0].split(',')[1]), 6)])

        print(lot_dispo2)
        
        distance_list = []
        for i in range(len(lot_dispo2)):
            coords = [list(reversed(map.curloc)), list(reversed(lot_dispo2[i]))]

            route = map.client.directions(coordinates=coords,
                                    profile='driving-car',
                                    format='geojson')

            self.distance = 0
            for i in range(0, len(route['features'][0]['geometry']['coordinates'])-1):
                self.distance += self.dist(route['features'][0]['geometry']['coordinates'][i], route['features'][0]['geometry']['coordinates'][i+1])
            distance_list.append(self.distance)
            
        self.destloc = lot_dispo2[distance_list.index(min(distance_list))]

        map.gps(map.curloc, self.destloc)
        self.web_view.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
        conn.close()
        
if __name__ == '__main__':
    import map
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
