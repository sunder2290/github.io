"""
Unit tests for Shop Simulator / Тесты для симулятора магазина
"""

import unittest
import os
import json
import tempfile
from shop_game import Item, Employee, Upgrade, Event, Customer, ShopState, GameEngine, get_default_catalog


class TestItem(unittest.TestCase):
    def test_item_creation_and_dict(self):
        item = Item("apple", "Яблоко", "Продукты", 10.0, 20.0, "Свежее яблоко", stock=50, selling_price=22.0)
        self.assertEqual(item.item_id, "apple")
        self.assertEqual(item.stock, 50)
        self.assertEqual(item.selling_price, 22.0)

        data = item.to_dict()
        restored = Item.from_dict(data)
        self.assertEqual(restored.name, "Яблоко")
        self.assertEqual(restored.base_cost, 10.0)
        self.assertEqual(restored.selling_price, 22.0)


class TestEmployee(unittest.TestCase):
    def test_employee_dict(self):
        emp = Employee("cashier1", "Анна", "Кассир", 800.0, 1.2, hired=False)
        self.assertFalse(emp.hired)

        data = emp.to_dict()
        restored = Employee.from_dict(data)
        self.assertEqual(restored.emp_id, "cashier1")
        self.assertEqual(restored.daily_salary, 800.0)


class TestUpgrade(unittest.TestCase):
    def test_upgrade_dict(self):
        upg = Upgrade("ac", "Кондиционер", 5000.0, "Комфорт", purchased=False, attractiveness_bonus=10.0)
        self.assertFalse(upg.purchased)

        data = upg.to_dict()
        restored = Upgrade.from_dict(data)
        self.assertEqual(restored.cost, 5000.0)
        self.assertEqual(restored.attractiveness_bonus, 10.0)


class TestGameEngine(unittest.TestCase):
    def setUp(self):
        items, employees, upgrades = get_default_catalog()
        state = ShopState(shop_name="Тестовый Магазин", money=10000.0, day=1, reputation=50.0, items=items, employees=employees, upgrades=upgrades)
        self.engine = GameEngine(state)

    def test_buy_stock_success(self):
        initial_money = self.engine.state.money
        initial_stock = self.engine.state.items["bread"].stock
        ok, msg = self.engine.buy_stock("bread", 10)
        self.assertTrue(ok)
        self.assertEqual(self.engine.state.items["bread"].stock, initial_stock + 10)
        self.assertEqual(self.engine.state.money, initial_money - (10 * 30.0))

    def test_buy_stock_insufficient_funds(self):
        self.engine.state.money = 100.0
        ok, msg = self.engine.buy_stock("gadget", 5)  # 5 * 1500 = 7500 > 100
        self.assertFalse(ok)
        self.assertIn("Недостаточно средств", msg)

    def test_buy_stock_invalid_quantity(self):
        ok, msg = self.engine.buy_stock("bread", -5)
        self.assertFalse(ok)

    def test_set_item_price(self):
        ok, msg = self.engine.set_item_price("bread", 65.0)
        self.assertTrue(ok)
        self.assertEqual(self.engine.state.items["bread"].selling_price, 65.0)

        ok_bad, msg_bad = self.engine.set_item_price("bread", -10.0)
        self.assertFalse(ok_bad)

    def test_hire_and_fire_employee(self):
        ok_hire, _ = self.engine.hire_employee("cashier1")
        self.assertTrue(ok_hire)
        self.assertTrue(self.engine.state.employees["cashier1"].hired)

        # Cannot hire twice
        ok_hire_again, _ = self.engine.hire_employee("cashier1")
        self.assertFalse(ok_hire_again)

        ok_fire, _ = self.engine.fire_employee("cashier1")
        self.assertTrue(ok_fire)
        self.assertFalse(self.engine.state.employees["cashier1"].hired)

    def test_buy_upgrade(self):
        ok, _ = self.engine.buy_upgrade("shelves")
        self.assertTrue(ok)
        self.assertTrue(self.engine.state.upgrades["shelves"].purchased)
        self.assertEqual(self.engine.state.money, 10000.0 - 3000.0)

    def test_simulate_day(self):
        # Ensure stock is available
        self.engine.buy_stock("bread", 50)
        self.engine.buy_stock("milk", 50)
        self.engine.hire_employee("cashier1")

        summary = self.engine.simulate_day()
        self.assertIn("day", summary)
        self.assertIn("revenue", summary)
        self.assertIn("net_profit", summary)
        self.assertEqual(self.engine.state.day, 2)
        self.assertEqual(len(self.engine.state.history), 1)


class TestShopStatePersistence(unittest.TestCase):
    def test_save_and_load(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
            tmp_path = tmp.name

        try:
            items, employees, upgrades = get_default_catalog()
            state = ShopState(shop_name="Сохраненный Магазин", money=15000.0, day=3, reputation=65.0, items=items, employees=employees, upgrades=upgrades)
            saved_ok = state.save_to_file(tmp_path)
            self.assertTrue(saved_ok)

            loaded = ShopState.load_from_file(tmp_path)
            self.assertIsNotNone(loaded)
            self.assertEqual(loaded.shop_name, "Сохраненный Магазин")
            self.assertEqual(loaded.money, 15000.0)
            self.assertEqual(loaded.day, 3)
            self.assertEqual(loaded.reputation, 65.0)
            self.assertIn("bread", loaded.items)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)


if __name__ == "__main__":
    unittest.main()
