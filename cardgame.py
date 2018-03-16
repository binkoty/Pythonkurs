from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from PyQt5.QtWidgets import *

class TableScene(QGraphicsScene):
    """ A scene with a table cloth background """
    def __init__(self):
        super().__init__()
        self.tile = QPixmap('cards/table.png')
        self.setBackgroundBrush(QBrush(self.tile))

class CardItem(QGraphicsSvgItem):
    """ A simple overloaded QGraphicsSvgItem that also stores the card position """
    def __init__(self, renderer, position):
        super().__init__()
        self.setSharedRenderer(renderer)
        self.position = position


class CardView(QGraphicsView):
    """ A View widget that represents the table area displaying a players cards. """

    # Underscores indicate a private function/method!
    def __read_cards(): # Ignore the PyCharm warning on this line. It's correct.
        """
        Reads all the 52 cards from files.
        :return: Dictionary of SVG renderers
        """
        all_cards = dict() # Dictionaries let us have convenient mappings between cards and their images
        for suit_file, suit in zip('CDHS', range(1,5)): # Check the order of the suits here!!! //HDSC org
            for value_file, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], range(2, 15)):
                file = value_file + suit_file
                key = (value, suit)  # I'm choosing this tuple to be the key for this dictionary
                all_cards[key] = QSvgRenderer('cards/' + file + '.svg')
        return all_cards

    # We read all the card graphics as static class variables
    back_card = QSvgRenderer('cards/Red_Back_2.svg')
    all_cards = __read_cards()

    def __init__(self, cards_model, card_spacing=250, padding=10):
        """
        Initializes the view to display the content of the given model
        :param cards_model: A model that represents a set of cards.
        The model should have: data_changed, cards, clicked_position, flipped,
        :param card_spacing: Spacing between the visualized cards.
        :param padding: Padding of table area around the visualized cards.
        """
        self.scene = TableScene()
        super().__init__(self.scene)

        self.model = cards_model
        self.card_spacing = card_spacing
        self.padding = padding

        # Whenever the this window should update, it should call the "change_cards" method.
        # This can, for example, be done by connecting it to a signal.
        # The view can listen to changes:
        cards_model.data_changed.connect(self.change_cards)
        cards_model.data_changed.connect(self.change_cards)
        # It is completely optional if you want to do it this way, or have some overreaching Player/GameState
        # call the "change_cards" method instead. z

        # Add the cards the first time around to represent the initial state.
        self.change_cards()

    def change_cards(self):
        # Add the cards from scratch
        self.scene.clear()
        for i, card in enumerate(self.model.hand):
            # The ID of the card in the dictionary of images is a tuple with (value, suit), both integers
            graphics_key = (card.value, card.suit)
            renderer = self.back_card if self.model.flipped(i) else self.all_cards[graphics_key]
            c = CardItem(renderer, i)

            # Shadow effects are cool!
            shadow = QGraphicsDropShadowEffect(c)
            shadow.setBlurRadius(10.)
            shadow.setOffset(5, 5)
            shadow.setColor(QColor(0, 0, 0, 180)) # Semi-transparent black!
            c.setGraphicsEffect(shadow)

            # Place the cards on the default positions
            c.setPos(c.position * self.card_spacing, 0)
            self.scene.addItem(c)

        self.update_view()

    def update_view(self):
        scale = (self.viewport().height()-2*self.padding)/313
        self.resetTransform()
        self.scale(scale, scale)
        # Put the scene bounding box
        self.setSceneRect(-self.padding//scale, -self.padding//scale,
                          self.viewport().width()//scale, self.viewport().height()//scale)

    def resizeEvent(self, painter):
        # This method is called when the window is resized.
        # If the widget is resize, we gotta adjust the card sizes.
        # QGraphicsView automatically re-paints everything when we modify the scene.
        self.update_view()
        super().resizeEvent(painter)

    # This is the Controller part of the GUI, handling input events that modify the Model
    def mousePressEvent(self, event):
        # We can check which item, if any, that we clicked on by fetching the scene items (neat!)
        pos = self.mapToScene(event.pos())
        item = self.scene.itemAt(pos, self.transform())
        if item is not None:
            # Report back that the user clicked on the card at given position:
            # The model can choose to do whatever it wants with this information.
            self.model.clicked_position(item.position)

class Buttons(QWidget):
    data_changed = pyqtSignal()

    #class containing the buttons for raising, folding and calling, also connects them to the appropriate method in the GameState class

    def __init__(self, state):
        super().__init__()
        self.RaiseButton = QPushButton("Raise 10€")
        self.CallButton = QPushButton("Call")
        self.FoldButton = QPushButton("Fold")
        self.RaiseButton.clicked.connect(state.raise_bet)
        self.CallButton.clicked.connect(state.call)
        self.FoldButton.clicked.connect(state.fold)


class Labels(QWidget):
    data_changed = pyqtSignal()

    #contains the labels, as well as a method for updating them (called upon whenever the gamestate changes)

    def __init__(self,state):
        super().__init__()
        self.state_model = state
        self.state_model.data_changed.connect(self.update_labels)
        self.min_bet_label = QLabel()
        self.pot_label = QLabel()
        self.bet_label = QLabel()
        self.credits_label = QLabel()
        self.update_labels()

    def update_labels(self):
        self.min_bet_label.setText('Minumum bet:' + str(self.state_model.inactive_player.bet))
        self.credits_label.setText('Credits:' + str(self.state_model.active_player.credits))
        self.pot_label.setText('Current Pot:' + str(self.state_model.pot))
        self.bet_label.setText('Currently Betted:' + str(self.state_model.active_player.bet))

