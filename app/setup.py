from distutils.core import setup
import py2exe
import kivy.utils
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.uix.button import Button,ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager,NoTransition,CardTransition
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from bar import Bar
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, OptionProperty, ListProperty, BooleanProperty, StringProperty, BoundedNumericProperty
from kivy.animation import Animation
from kivy.lang import Builder

setup(windows=['main.py'])
