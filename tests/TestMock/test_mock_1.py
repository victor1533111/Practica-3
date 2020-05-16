import unittest
from src.Flights import Flights
from src.User import User
from unittest import mock
from requests.exceptions import Timeout

class TestMock1(unittest.TestCase):
     
    @mock.patch('src.Flights')
    def test_confirmarvuelos(self,mock_vuelos):
        self.assertTrue(mock_vuelos.confirmarvuelos(mock_vuelos.usuario,mock_vuelos.self))
        mock_vuelos.confirmarvuelos(mock_vuelos.usuario,mock_vuelos.self).return_value = False
        self.assertFalse(mock_vuelos.confirmarvuelos(mock_vuelos.usuario,mock_vuelos.self))
        