import sys
import unreal
import os
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QMouseEvent
from PyQt5 import uic, QtCore
"""
actors_num = int(float(sys.argv[1]))    # Get the number of actors to spawn from command line argument 1
rotation_value = int(float(sys.argv[2]))    # Get the rotation value for each actor from command line argument 2
offset_pos_value = float(sys.argv[3])   # Get the offset position value for each actor from command line argument 3
"""
def actor_creator(actors_num, rotation_value, offset_pos_value):
    text_display = 'Spawning actors in the level'  # Text to display in the progress dialog

    # Get the currently selected asset in the Unreal Editor
    editor_util = unreal.EditorUtilityLibrary()
    selected_asset = editor_util.get_selected_assets()

    # Spawn the specified number of actors, with specified rotation and position offsets
    # using the selected asset as a template
    with unreal.ScopedSlowTask(actors_num, text_display) as st:
        st.make_dialog(True)
        for i in range(actors_num):
            if st.should_cancel():
                break
            # Spawn an actor in the level using the selected asset as a template
            # with a position offset and rotation offset
            unreal.EditorLevelLibrary.spawn_actor_from_object(selected_asset[0],
                                                              unreal.Vector(offset_pos_value * i, offset_pos_value * i,
                                                                            25.0),
                                                              unreal.Rotator(0.0, 0.0, rotation_value * i))
            # Log that a new actor was added to the level
            unreal.log("Added a new actor in the level")
            # Enter a new progress frame in the progress dialog
            st.enter_progress_frame(1)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r"F:\PycharmProjects\UE\ue-actor-creator\actor-duplicator.ui", self)

        # Spinbox
        self.spinbox = self.findChild(QSpinBox, "spinBox")
        self.rotation = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.offset = self.findChild(QDoubleSpinBox, "doubleSpinBox_2")

        # Buttons
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.duplicate)

    def duplicate(self):
        num_actors = self.spinbox.value()
        rotation = self.rotation.value()
        offset = self.offset.value()
        actor_creator(num_actors, rotation, offset)
        QApplication.quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
