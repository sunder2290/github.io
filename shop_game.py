"""
Shop Simulator / Симулятор Магазина
Игровой движок, CLI и Tkinter GUI интерфейс.
"""

import json
import random
import os
import sys
import math
from typing import Dict, List, Optional, Any, Tuple

# Tkinter imports for GUI
import tkinter as tk
from tkinter import ttk, messagebox


class Item:
    """Товар в магазине"""

    def __init__(
        self,
        item_id: str,
        name: str,
        category: str,
        base_cost: float,
        suggested_price: float,
        description: str,
        stock: int = 0,
        selling_price: float = 0.0,
    ):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.base_cost = base_cost
        self.suggested_price = suggested_price
        self.description = description
        self.stock = stock
        self.selling_price = selling_price if selling_price > 0 else suggested_price

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "category": self.category,
            "base_cost": self.base_cost,
            "suggested_price": self.suggested_price,
            "description": self.description,
            "stock": self.stock,
            "selling_price": self.selling_price,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Item":
        return cls(
            item_id=data["item_id"],
            name=data["name"],
            category=data["category"],
            base_cost=float(data["base_cost"]),
            suggested_price=float(data["suggested_price"]),
            description=data["description"],
            stock=int(data["stock"]),
            selling_price=float(data["selling_price"]),
        )


class Employee:
    """Сотрудник магазина"""

    def __init__(
        self,
        emp_id: str,
        name: str,
        role: str,
        daily_salary: float,
        efficiency_bonus: float,
        hired: bool = False,
    ):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.daily_salary = daily_salary
        self.efficiency_bonus = efficiency_bonus
        self.hired = hired

    def to_dict(self) -> Dict[str, Any]:
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "role": self.role,
            "daily_salary": self.daily_salary,
            "efficiency_bonus": self.efficiency_bonus,
            "hired": self.hired,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Employee":
        return cls(
            emp_id=data["emp_id"],
            name=data["name"],
            role=data["role"],
            daily_salary=float(data["daily_salary"]),
            efficiency_bonus=float(data["efficiency_bonus"]),
            hired=bool(data["hired"]),
        )


class Upgrade:
    """Улучшение магазина"""

    def __init__(
        self,
        upg_id: str,
        name: str,
        cost: float,
        description: str,
        purchased: bool = False,
        capacity_bonus: int = 0,
        attractiveness_bonus: float = 0.0,
    ):
        self.upg_id = upg_id
        self.name = name
        self.cost = cost
        self.description = description
        self.purchased = purchased
        self.capacity_bonus = capacity_bonus
        self.attractiveness_bonus = attractiveness_bonus

    def to_dict(self) -> Dict[str, Any]:
        return {
            "upg_id": self.upg_id,
            "name": self.name,
            "cost": self.cost,
            "description": self.description,
            "purchased": self.purchased,
            "capacity_bonus": self.capacity_bonus,
            "attractiveness_bonus": self.attractiveness_bonus,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Upgrade":
        return cls(
            upg_id=data["upg_id"],
            name=data["name"],
            cost=float(data["cost"]),
            description=data["description"],
            purchased=bool(data["purchased"]),
            capacity_bonus=int(data.get("capacity_bonus", 0)),
            attractiveness_bonus=float(data.get("attractiveness_bonus", 0.0)),
        )


class Customer:
    """Покупатель в симуляции"""

    def __init__(self, name: str, budget: float, price_sensitivity: float, target_category: Optional[str] = None):
        self.name = name
        self.budget = budget
        self.price_sensitivity = price_sensitivity
        self.target_category = target_category


class Event:
    """Случайное событие дня"""

    def __init__(self, event_id: str, title: str, description: str, impact_type: str, multiplier: float):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.impact_type = impact_type
        self.multiplier = multiplier

    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "impact_type": self.impact_type,
            "multiplier": self.multiplier,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Event":
        return cls(
            event_id=data["event_id"],
            title=data["title"],
            description=data["description"],
            impact_type=data["impact_type"],
            multiplier=float(data["multiplier"]),
        )


class ShopState:
    """Состояние магазина и данные сохранения"""

    def __init__(
        self,
        shop_name: str = "Мой Супермаркет",
        money: float = 10000.0,
        day: int = 1,
        reputation: float = 50.0,
        items: Optional[Dict[str, Item]] = None,
        employees: Optional[Dict[str, Employee]] = None,
        upgrades: Optional[Dict[str, Upgrade]] = None,
        history: Optional[List[Dict[str, Any]]] = None,
    ):
        self.shop_name = shop_name
        self.money = money
        self.day = day
        self.reputation = max(0.0, min(100.0, reputation))
        self.items = items if items is not None else {}
        self.employees = employees if employees is not None else {}
        self.upgrades = upgrades if upgrades is not None else {}
        self.history = history if history is not None else []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "shop_name": self.shop_name,
            "money": self.money,
            "day": self.day,
            "reputation": self.reputation,
            "items": {k: v.to_dict() for k, v in self.items.items()},
            "employees": {k: v.to_dict() for k, v in self.employees.items()},
            "upgrades": {k: v.to_dict() for k, v in self.upgrades.items()},
            "history": self.history,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ShopState":
        items = {k: Item.from_dict(v) for k, v in data.get("items", {}).items()}
        employees = {k: Employee.from_dict(v) for k, v in data.get("employees", {}).items()}
        upgrades = {k: Upgrade.from_dict(v) for k, v in data.get("upgrades", {}).items()}
        return cls(
            shop_name=data.get("shop_name", "Мой Супермаркет"),
            money=float(data.get("money", 10000.0)),
            day=int(data.get("day", 1)),
            reputation=float(data.get("reputation", 50.0)),
            items=items,
            employees=employees,
            upgrades=upgrades,
            history=data.get("history", []),
        )

    def save_to_file(self, filepath: str = "savegame.json") -> bool:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False

    @classmethod
    def load_from_file(cls, filepath: str = "savegame.json") -> Optional["ShopState"]:
        if not os.path.exists(filepath):
            return None
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return cls.from_dict(data)
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return None


def get_default_catalog() -> Tuple[Dict[str, Item], Dict[str, Employee], Dict[str, Upgrade]]:
    items = {
        "bread": Item("bread", "Свежий Хлеб", "Продукты", 30.0, 50.0, "Базовый продукт питания.", stock=20),
        "milk": Item("milk", "Молоко 3.2%", "Продукты", 50.0, 80.0, "Свежее фермерское молоко.", stock=15),
        "coffee": Item("coffee", "Зерновой Кофе", "Напитки", 300.0, 550.0, "Ароматный премиум кофе.", stock=10),
        "cheese": Item("cheese", "Сыр Голландский", "Продукты", 200.0, 380.0, "Выдержанный сыр высшего качества.", stock=8),
        "tea": Item("tea", "Чай Зеленый", "Напитки", 80.0, 150.0, "Листовой зеленый чай.", stock=12),
        "gadget": Item("gadget", "Беспроводные Наушники", "Электроника", 1500.0, 2900.0, "Популярный гаджет.", stock=5),
        "phone_charger": Item("phone_charger", "Быстрая Зарядка", "Электроника", 400.0, 850.0, "Качественный кабель и адаптер.", stock=10),
        "chocolate": Item("chocolate", "Шоколад Темный", "Сладости", 70.0, 130.0, "Элитный плиточный шоколад.", stock=25),
    }

    employees = {
        "cashier1": Employee("cashier1", "Анна Смирнова", "Кассир", 800.0, 1.2, hired=False),
        "marketer1": Employee("marketer1", "Игорь Соколов", "Маркетолог", 1500.0, 1.35, hired=False),
        "security1": Employee("security1", "Василий Петров", "Охранник", 1000.0, 0.8, hired=False),
        "manager1": Employee("manager1", "Елена Кузнецова", "Менеджер", 2000.0, 1.25, hired=False),
    }

    upgrades = {
        "shelves": Upgrade("shelves", "Новые стеллажи", 3000.0, "Увеличивают вместимость и привлекательность товаров.", capacity_bonus=50, attractiveness_bonus=5.0),
        "ac": Upgrade("ac", "Кондиционер", 5000.0, "Покупатели чувствуют себя комфортно и чаще делают покупки.", attractiveness_bonus=10.0),
        "checkout": Upgrade("checkout", "Быстрая касса", 7000.0, "Сокращает очереди и повышает удовлетворенность.", attractiveness_bonus=8.0),
        "cctv": Upgrade("cctv", "Система видеонаблюдения", 6000.0, "Защищает магазин от краж и убытков.", attractiveness_bonus=2.0),
        "billboard": Upgrade("billboard", "Рекламный щит", 10000.0, "Привлекает большой поток новых клиентов.", attractiveness_bonus=18.0),
    }

    return items, employees, upgrades


class GameEngine:
    """Главный управляющий класс бизнес-логики и симуляции"""

    def __init__(self, state: Optional[ShopState] = None):
        if state is not None:
            self.state = state
        else:
            items, employees, upgrades = get_default_catalog()
            self.state = ShopState(items=items, employees=employees, upgrades=upgrades)

    def buy_stock(self, item_id: str, quantity: int) -> Tuple[bool, str]:
        if quantity <= 0:
            return False, "Количество должно быть больше нуля."
        if item_id not in self.state.items:
            return False, "Товар не найден."

        item = self.state.items[item_id]
        total_cost = item.base_cost * quantity

        if self.state.money < total_cost:
            return False, f"Недостаточно средств! Требуется {total_cost:.2f} ₽, доступно {self.state.money:.2f} ₽."

        self.state.money -= total_cost
        item.stock += quantity
        return True, f"Успешно закуплено {quantity} шт. '{item.name}' на сумму {total_cost:.2f} ₽."

    def set_item_price(self, item_id: str, new_price: float) -> Tuple[bool, str]:
        if new_price <= 0:
            return False, "Цена должна быть больше нуля."
        if item_id not in self.state.items:
            return False, "Товар не найден."

        item = self.state.items[item_id]
        item.selling_price = new_price
        return True, f"Цена на '{item.name}' установлена: {new_price:.2f} ₽."

    def hire_employee(self, emp_id: str) -> Tuple[bool, str]:
        if emp_id not in self.state.employees:
            return False, "Сотрудник не найден."
        emp = self.state.employees[emp_id]
        if emp.hired:
            return False, "Сотрудник уже нанят."

        emp.hired = True
        return True, f"Сотрудник {emp.name} ({emp.role}) успешно нанят!"

    def fire_employee(self, emp_id: str) -> Tuple[bool, str]:
        if emp_id not in self.state.employees:
            return False, "Сотрудник не найден."
        emp = self.state.employees[emp_id]
        if not emp.hired:
            return False, "Сотрудник не работает в магазине."

        emp.hired = False
        return True, f"Сотрудник {emp.name} уволен."

    def buy_upgrade(self, upg_id: str) -> Tuple[bool, str]:
        if upg_id not in self.state.upgrades:
            return False, "Улучшение не найдено."
        upg = self.state.upgrades[upg_id]
        if upg.purchased:
            return False, "Улучшение уже приобретено."

        if self.state.money < upg.cost:
            return False, f"Недостаточно средств! Стоимость {upg.cost:.2f} ₽."

        self.state.money -= upg.cost
        upg.purchased = True
        self.state.reputation = min(100.0, self.state.reputation + upg.attractiveness_bonus)
        return True, f"Приобретено улучшение '{upg.name}'!"

    def _generate_event(self) -> Optional[Event]:
        if random.random() > 0.35:
            return None

        events = [
            Event("surge", "Ажиотажный спрос", "Поток клиентов резко возрос из-за праздника!", "demand", 1.5),
            Event("bad_weather", "Плохая погода", "Сильный дождь удержал многих дома.", "demand", 0.7),
            Event("supplier_discount", "Скидка от поставщиков", "Поставщики снизили закупочные цены!", "cost", 0.8),
            Event("inspection", "Проверка инспекции", "Штраф за мелкие нарушения.", "cash", -1000.0),
            Event("theft", "Мелкое хищение", "Из магазина пропала часть товара.", "theft", 0.1),
        ]
        return random.choice(events)

    def simulate_day(self) -> Dict[str, Any]:
        day_num = self.state.day
        event = self._generate_event()

        salaries = sum(emp.daily_salary for emp in self.state.employees.values() if emp.hired)
        self.state.money -= salaries

        attr_bonus = sum(u.attractiveness_bonus for u in self.state.upgrades.values() if u.purchased)
        marketing_bonus = 1.0
        for emp in self.state.employees.values():
            if emp.hired and emp.role == "Маркетолог":
                marketing_bonus *= emp.efficiency_bonus

        demand_mult = event.multiplier if (event and event.impact_type == "demand") else 1.0
        num_customers = int((15 + self.state.reputation * 0.8 + attr_bonus * 1.2) * marketing_bonus * demand_mult)
        num_customers = max(5, num_customers)

        theft_loss = 0.0
        has_security = any(e.hired and e.role == "Охранник" for e in self.state.employees.values())
        has_cctv = self.state.upgrades.get("cctv", Upgrade("cctv", "", 0, "")).purchased

        if event and event.impact_type == "theft":
            if not has_security and not has_cctv:
                for item in self.state.items.values():
                    stolen = int(item.stock * event.multiplier)
                    item.stock -= stolen
                    theft_loss += stolen * item.base_cost

        if event and event.impact_type == "cash":
            self.state.money += event.multiplier

        total_revenue = 0.0
        total_items_sold = 0
        satisfied_customers = 0
        unsatisfied_customers = 0

        categories = list(set(item.category for item in self.state.items.values()))

        for i in range(num_customers):
            target_cat = random.choice(categories) if categories else None
            budget = random.uniform(200.0, 2500.0)
            sensitivity = random.uniform(0.6, 1.4)
            cust = Customer(f"Покупатель #{i+1}", budget, sensitivity, target_cat)

            available_items = [it for it in self.state.items.values() if it.stock > 0]
            if target_cat:
                cat_items = [it for it in available_items if it.category == target_cat]
                if cat_items:
                    available_items = cat_items

            if not available_items:
                unsatisfied_customers += 1
                continue

            bought_something = False
            random.shuffle(available_items)

            for item in available_items:
                if item.stock <= 0:
                    continue

                price_ratio = item.selling_price / item.suggested_price
                buy_probability = max(0.05, min(0.95, 1.0 - (price_ratio - 1.0) * cust.price_sensitivity))

                if item.selling_price <= cust.budget and random.random() < buy_probability:
                    max_qty = min(item.stock, int(cust.budget // item.selling_price), random.randint(1, 3))
                    if max_qty > 0:
                        item.stock -= max_qty
                        cost_sum = max_qty * item.selling_price
                        cust.budget -= cost_sum
                        total_revenue += cost_sum
                        total_items_sold += max_qty
                        bought_something = True

            if bought_something:
                satisfied_customers += 1
            else:
                unsatisfied_customers += 1

        self.state.money += total_revenue

        if satisfied_customers + unsatisfied_customers > 0:
            satisfaction_rate = satisfied_customers / (satisfied_customers + unsatisfied_customers)
            if satisfaction_rate > 0.7:
                self.state.reputation = min(100.0, self.state.reputation + 1.5)
            elif satisfaction_rate < 0.4:
                self.state.reputation = max(0.0, self.state.reputation - 2.0)

        daily_profit = total_revenue - salaries - theft_loss

        summary = {
            "day": day_num,
            "revenue": total_revenue,
            "salaries": salaries,
            "theft_loss": theft_loss,
            "net_profit": daily_profit,
            "items_sold": total_items_sold,
            "customers_count": num_customers,
            "satisfied": satisfied_customers,
            "unsatisfied": unsatisfied_customers,
            "reputation": self.state.reputation,
            "event": event.to_dict() if event else None,
            "money_after": self.state.money,
        }

        self.state.history.append(summary)
        self.state.day += 1
        self.state.save_to_file()

        return summary


class ShopGUI:
    """Графический интерфейс на Tkinter"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Симулятор Магазина")
        self.root.geometry("950x650")
        self.root.minsize(800, 550)

        # Попытка загрузки сохранения
        loaded = ShopState.load_from_file()
        if loaded:
            self.engine = GameEngine(loaded)
        else:
            self.engine = GameEngine()

        self.create_widgets()
        self.refresh_ui()

    def create_widgets(self):
        # Панель верхнего статуса (Header)
        header_frame = ttk.Frame(self.root, padding=10, relief=tk.RAISED)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        self.title_label = ttk.Label(header_frame, text="", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=4, sticky=tk.W, pady=(0, 5))

        self.lbl_day = ttk.Label(header_frame, text="День: 1", font=("Helvetica", 11, "bold"))
        self.lbl_day.grid(row=1, column=0, padx=10, sticky=tk.W)

        self.lbl_money = ttk.Label(header_frame, text="Баланс: 0 ₽", font=("Helvetica", 11, "bold"), foreground="green")
        self.lbl_money.grid(row=1, column=1, padx=10, sticky=tk.W)

        self.lbl_reputation = ttk.Label(header_frame, text="Репутация: 50%", font=("Helvetica", 11))
        self.lbl_reputation.grid(row=1, column=2, padx=10, sticky=tk.W)

        btn_next_day = ttk.Button(header_frame, text="⏩ Прожить день", command=self.on_simulate_day)
        btn_next_day.grid(row=1, column=3, padx=10, sticky=tk.E)

        btn_save = ttk.Button(header_frame, text="💾 Сохранить", command=self.on_save)
        btn_save.grid(row=1, column=4, padx=5, sticky=tk.E)

        # Главная область закладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Вкладка 1: Дашборд / Обзор
        self.tab_dashboard = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_dashboard, text="📊 Дашборд")
        self.setup_dashboard_tab()

        # Вкладка 2: Склад и Цены
        self.tab_inventory = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_inventory, text="📦 Склад и Цены")
        self.setup_inventory_tab()

        # Вкладка 3: Персонал
        self.tab_staff = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_staff, text="👥 Персонал")
        self.setup_staff_tab()

        # Вкладка 4: Улучшения
        self.tab_upgrades = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_upgrades, text="🛠️ Улучшения")
        self.setup_upgrades_tab()

        # Вкладка 5: История и Отчеты
        self.tab_history = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_history, text="📈 История продаж")
        self.setup_history_tab()

    def setup_dashboard_tab(self):
        left_frame = ttk.LabelFrame(self.tab_dashboard, text="Информация о магазине", padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.dash_info_text = tk.Text(left_frame, wrap=tk.WORD, height=12, width=40)
        self.dash_info_text.pack(fill=tk.BOTH, expand=True)

        right_frame = ttk.LabelFrame(self.tab_dashboard, text="Лента событий и результатов", padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.dash_log_text = tk.Text(right_frame, wrap=tk.WORD, height=12, width=40)
        self.dash_log_text.pack(fill=tk.BOTH, expand=True)

    def setup_inventory_tab(self):
        columns = ("id", "name", "cat", "stock", "cost", "price", "suggested")
        self.tree_items = ttk.Treeview(self.tab_inventory, columns=columns, show="headings", height=10)
        self.tree_items.heading("id", text="ID")
        self.tree_items.heading("name", text="Товар")
        self.tree_items.heading("cat", text="Категория")
        self.tree_items.heading("stock", text="На складе")
        self.tree_items.heading("cost", text="Закупочная цена")
        self.tree_items.heading("price", text="Розничная цена")
        self.tree_items.heading("suggested", text="Реком. цена")

        self.tree_items.column("id", width=60)
        self.tree_items.column("name", width=160)
        self.tree_items.column("cat", width=100)
        self.tree_items.column("stock", width=80)
        self.tree_items.column("cost", width=100)
        self.tree_items.column("price", width=100)
        self.tree_items.column("suggested", width=100)

        self.tree_items.pack(fill=tk.BOTH, expand=True, pady=5)

        # Панель действия с товаром
        controls_frame = ttk.LabelFrame(self.tab_inventory, text="Управление выбранным товаром", padding=10)
        controls_frame.pack(fill=tk.X, pady=5)

        ttk.Label(controls_frame, text="Количество закупки:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_buy_qty = ttk.Entry(controls_frame, width=10)
        self.entry_buy_qty.insert(0, "10")
        self.entry_buy_qty.grid(row=0, column=1, padx=5, pady=5)

        btn_buy = ttk.Button(controls_frame, text="Закупить товар", command=self.on_buy_stock)
        btn_buy.grid(row=0, column=2, padx=10, pady=5)

        ttk.Label(controls_frame, text="Новая цена:").grid(row=0, column=3, padx=5, pady=5)
        self.entry_new_price = ttk.Entry(controls_frame, width=10)
        self.entry_new_price.grid(row=0, column=4, padx=5, pady=5)

        btn_price = ttk.Button(controls_frame, text="Изменить цену", command=self.on_set_price)
        btn_price.grid(row=0, column=5, padx=10, pady=5)

    def setup_staff_tab(self):
        columns = ("id", "name", "role", "salary", "bonus", "status")
        self.tree_staff = ttk.Treeview(self.tab_staff, columns=columns, show="headings", height=10)
        self.tree_staff.heading("id", text="ID")
        self.tree_staff.heading("name", text="Имя")
        self.tree_staff.heading("role", text="Должность")
        self.tree_staff.heading("salary", text="З/П в день")
        self.tree_staff.heading("bonus", text="Эффективность")
        self.tree_staff.heading("status", text="Статус")

        self.tree_staff.pack(fill=tk.BOTH, expand=True, pady=5)

        controls_frame = ttk.Frame(self.tab_staff, padding=10)
        controls_frame.pack(fill=tk.X, pady=5)

        btn_hire = ttk.Button(controls_frame, text="Нанять сотрудника", command=self.on_hire_staff)
        btn_hire.pack(side=tk.LEFT, padx=10)

        btn_fire = ttk.Button(controls_frame, text="Уволить сотрудника", command=self.on_fire_staff)
        btn_fire.pack(side=tk.LEFT, padx=10)

    def setup_upgrades_tab(self):
        columns = ("id", "name", "cost", "effect", "status")
        self.tree_upgrades = ttk.Treeview(self.tab_upgrades, columns=columns, show="headings", height=10)
        self.tree_upgrades.heading("id", text="ID")
        self.tree_upgrades.heading("name", text="Улучшение")
        self.tree_upgrades.heading("cost", text="Стоимость")
        self.tree_upgrades.heading("effect", text="Описание / Эффект")
        self.tree_upgrades.heading("status", text="Статус")

        self.tree_upgrades.column("id", width=60)
        self.tree_upgrades.column("name", width=180)
        self.tree_upgrades.column("cost", width=100)
        self.tree_upgrades.column("effect", width=350)
        self.tree_upgrades.column("status", width=100)

        self.tree_upgrades.pack(fill=tk.BOTH, expand=True, pady=5)

        controls_frame = ttk.Frame(self.tab_upgrades, padding=10)
        controls_frame.pack(fill=tk.X, pady=5)

        btn_buy_upg = ttk.Button(controls_frame, text="Приобрести улучшение", command=self.on_buy_upgrade)
        btn_buy_upg.pack(side=tk.LEFT, padx=10)

    def setup_history_tab(self):
        columns = ("day", "revenue", "salaries", "loss", "profit", "sold", "satisfied", "reputation")
        self.tree_history = ttk.Treeview(self.tab_history, columns=columns, show="headings", height=12)
        self.tree_history.heading("day", text="День")
        self.tree_history.heading("revenue", text="Выручка")
        self.tree_history.heading("salaries", text="Зарплаты")
        self.tree_history.heading("loss", text="Убытки")
        self.tree_history.heading("profit", text="Прибыль")
        self.tree_history.heading("sold", text="Продано шт.")
        self.tree_history.heading("satisfied", text="Довольных")
        self.tree_history.heading("reputation", text="Репутация")

        self.tree_history.pack(fill=tk.BOTH, expand=True, pady=5)

    def refresh_ui(self):
        # Обновление заголовка
        self.title_label.config(text=f"🛒 {self.engine.state.shop_name}")
        self.lbl_day.config(text=f"День: {self.engine.state.day}")
        self.lbl_money.config(text=f"Баланс: {self.engine.state.money:.2f} ₽")
        self.lbl_reputation.config(text=f"Репутация: {self.engine.state.reputation:.1f}%")

        # Обновление Дашборда
        self.dash_info_text.delete("1.0", tk.END)
        hired_count = sum(1 for e in self.engine.state.employees.values() if e.hired)
        upg_count = sum(1 for u in self.engine.state.upgrades.values() if u.purchased)
        info = (
            f"Название магазина: {self.engine.state.shop_name}\n"
            f"Текущий день: {self.engine.state.day}\n"
            f"Капитал: {self.engine.state.money:.2f} ₽\n"
            f"Уровень репутации: {self.engine.state.reputation:.1f}%\n"
            f"Нанято сотрудников: {hired_count} чел.\n"
            f"Куплено улучшений: {upg_count} шт.\n\n"
            f"Полезный совет:\n"
            f"Не завышайте цены слишком сильно относительно рекомендуемых, "
            f"иначе покупатели будут уходить без покупок и репутация снизится!"
        )
        self.dash_info_text.insert(tk.END, info)

        # Обновление логотипа / истории на дашборде
        self.dash_log_text.delete("1.0", tk.END)
        if self.engine.state.history:
            for log in reversed(self.engine.state.history[-10:]):
                evt_str = f" [Событие: {log['event']['title']}]" if log['event'] else ""
                msg = f"День {log['day']}: Выручка {log['revenue']:.2f} ₽ | Прибыль {log['net_profit']:.2f} ₽{evt_str}\n"
                self.dash_log_text.insert(tk.END, msg)
        else:
            self.dash_log_text.insert(tk.END, "Добро пожаловать в Симулятор Магазина!\nНажмите 'Прожить день', чтобы запустить торговлю.")

        # Обновление списка товаров
        for row in self.tree_items.get_children():
            self.tree_items.delete(row)
        for item in self.engine.state.items.values():
            self.tree_items.insert(
                "",
                tk.END,
                values=(
                    item.item_id,
                    item.name,
                    item.category,
                    item.stock,
                    f"{item.base_cost:.2f} ₽",
                    f"{item.selling_price:.2f} ₽",
                    f"{item.suggested_price:.2f} ₽",
                ),
            )

        # Обновление персонала
        for row in self.tree_staff.get_children():
            self.tree_staff.delete(row)
        for emp in self.engine.state.employees.values():
            status = "Работает" if emp.hired else "Доступен"
            self.tree_staff.insert(
                "",
                tk.END,
                values=(emp.emp_id, emp.name, emp.role, f"{emp.daily_salary:.2f} ₽", f"x{emp.efficiency_bonus}", status),
            )

        # Обновление улучшений
        for row in self.tree_upgrades.get_children():
            self.tree_upgrades.delete(row)
        for upg in self.engine.state.upgrades.values():
            status = "Приобретено" if upg.purchased else "Доступно"
            self.tree_upgrades.insert(
                "",
                tk.END,
                values=(upg.upg_id, upg.name, f"{upg.cost:.2f} ₽", upg.description, status),
            )

        # Обновление таблицы истории
        for row in self.tree_history.get_children():
            self.tree_history.delete(row)
        for log in reversed(self.engine.state.history):
            self.tree_history.insert(
                "",
                tk.END,
                values=(
                    log["day"],
                    f"{log['revenue']:.2f} ₽",
                    f"{log['salaries']:.2f} ₽",
                    f"{log['theft_loss']:.2f} ₽",
                    f"{log['net_profit']:.2f} ₽",
                    log["items_sold"],
                    f"{log['satisfied']}/{log['customers_count']}",
                    f"{log['reputation']:.1f}%",
                ),
            )

    def on_buy_stock(self):
        selected = self.tree_items.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите товар из таблицы!")
            return
        item_id = self.tree_items.item(selected[0])["values"][0]
        try:
            qty = int(self.entry_buy_qty.get().strip())
            ok, msg = self.engine.buy_stock(str(item_id), qty)
            if ok:
                messagebox.showinfo("Успех", msg)
            else:
                messagebox.showerror("Ошибка", msg)
            self.refresh_ui()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число товаров!")

    def on_set_price(self):
        selected = self.tree_items.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите товар из таблицы!")
            return
        item_id = self.tree_items.item(selected[0])["values"][0]
        try:
            price = float(self.entry_new_price.get().strip())
            ok, msg = self.engine.set_item_price(str(item_id), price)
            if ok:
                messagebox.showinfo("Успех", msg)
            else:
                messagebox.showerror("Ошибка", msg)
            self.refresh_ui()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректную цену!")

    def on_hire_staff(self):
        selected = self.tree_staff.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите сотрудника!")
            return
        emp_id = str(self.tree_staff.item(selected[0])["values"][0])
        ok, msg = self.engine.hire_employee(emp_id)
        if ok:
            messagebox.showinfo("Персонал", msg)
        else:
            messagebox.showwarning("Предупреждение", msg)
        self.refresh_ui()

    def on_fire_staff(self):
        selected = self.tree_staff.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите сотрудника!")
            return
        emp_id = str(self.tree_staff.item(selected[0])["values"][0])
        ok, msg = self.engine.fire_employee(emp_id)
        if ok:
            messagebox.showinfo("Персонал", msg)
        else:
            messagebox.showwarning("Предупреждение", msg)
        self.refresh_ui()

    def on_buy_upgrade(self):
        selected = self.tree_upgrades.selection()
        if not selected:
            messagebox.showwarning("Внимание", "Выберите улучшение!")
            return
        upg_id = str(self.tree_upgrades.item(selected[0])["values"][0])
        ok, msg = self.engine.buy_upgrade(upg_id)
        if ok:
            messagebox.showinfo("Улучшения", msg)
        else:
            messagebox.showwarning("Предупреждение", msg)
        self.refresh_ui()

    def on_simulate_day(self):
        summary = self.engine.simulate_day()
        self.refresh_ui()

        evt_text = ""
        if summary["event"]:
            evt_text = f"\n\n⚡ Событие дня: {summary['event']['title']}\n{summary['event']['description']}"

        msg = (
            f"День #{summary['day']} завершен!\n\n"
            f"Пришло покупателей: {summary['customers_count']}\n"
            f"Довольных: {summary['satisfied']}, Без покупок: {summary['unsatisfied']}\n"
            f"Выручка: +{summary['revenue']:.2f} ₽\n"
            f"Зарплаты: -{summary['salaries']:.2f} ₽\n"
            f"Убытки от краж: -{summary['theft_loss']:.2f} ₽\n"
            f"Чистая прибыль: {summary['net_profit']:.2f} ₽"
            f"{evt_text}"
        )
        messagebox.showinfo("Итоги дня", msg)

    def on_save(self):
        if self.engine.state.save_to_file():
            messagebox.showinfo("Сохранение", "Состояние игры успешно сохранено!")


def run_gui():
    root = tk.Tk()
    app = ShopGUI(root)
    root.mainloop()


def run_cli():
    """Консольный интерфейс игры"""
    loaded_state = ShopState.load_from_file()
    if loaded_state:
        print("Найдено сохранение. Загрузить сохранение? (y/n): ", end="")
        ans = input().strip().lower()
        if ans == "y":
            engine = GameEngine(loaded_state)
            print("Сохранение успешно загружено!")
        else:
            engine = GameEngine()
    else:
        engine = GameEngine()

    while True:
        print("\n" + "=" * 50)
        print(f"   СИМУЛЯТОР МАГА3ИНА | {engine.state.shop_name}")
        print(f"   День: {engine.state.day} | Баланс: {engine.state.money:.2f} ₽ | Репутация: {engine.state.reputation:.1f}%")
        print("=" * 50)
        print("1. Обзор склада и закупка товаров")
        print("2. Установка розничных цен")
        print("3. Управление персоналом")
        print("4. Магазин улучшений")
        print("5. Запустить симуляцию следующего дня")
        print("6. История доходов и отчетов")
        print("7. Сохранить игру")
        print("8. Переименовать магазин")
        print("0. Выйти из игры")
        print("-" * 50)

        choice = input("Выберите действие (0-8): ").strip()

        if choice == "1":
            print("\n--- ТОВАРЫ НА СКЛАДЕ И ЗАКУПКА ---")
            for item in engine.state.items.values():
                print(f"[{item.item_id}] {item.name} | На складе: {item.stock} шт. | Закуп: {item.base_cost:.2f} ₽ | Продажа: {item.selling_price:.2f} ₽ (Реком.: {item.suggested_price:.2f} ₽)")
            item_id = input("\nВведите ID товара для закупки (или Enter для отмены): ").strip()
            if item_id in engine.state.items:
                try:
                    qty = int(input("Введите количество для закупки: ").strip())
                    ok, msg = engine.buy_stock(item_id, qty)
                    print(f"\n>> {msg}")
                except ValueError:
                    print("\n>> Некорректное число.")
            elif item_id:
                print("\n>> Товар с таким ID не найден.")

        elif choice == "2":
            print("\n--- УСТАНОВКА РОЗНИЧНЫХ ЦЕН ---")
            for item in engine.state.items.values():
                print(f"[{item.item_id}] {item.name} | Текущая цена: {item.selling_price:.2f} ₽ | Рекоменд.: {item.suggested_price:.2f} ₽")
            item_id = input("\nВведите ID товара для изменения цены (или Enter для отмены): ").strip()
            if item_id in engine.state.items:
                try:
                    price = float(input("Введите новую цену: ").strip())
                    ok, msg = engine.set_item_price(item_id, price)
                    print(f"\n>> {msg}")
                except ValueError:
                    print("\n>> Некорректная цена.")
            elif item_id:
                print("\n>> Товар с таким ID не найден.")

        elif choice == "3":
            print("\n--- УПРАВЛЕНИЕ ПЕРСОНАЛОМ ---")
            for emp in engine.state.employees.values():
                status = "НАНЯТ" if emp.hired else "ДОСТУПЕН"
                print(f"[{emp.emp_id}] {emp.name} ({emp.role}) | З/П в день: {emp.daily_salary:.2f} ₽ | Статус: {status}")
            emp_id = input("\nВведите ID сотрудника (или Enter для отмены): ").strip()
            if emp_id in engine.state.employees:
                emp = engine.state.employees[emp_id]
                if emp.hired:
                    action = input(f"Уволить сотрудника {emp.name}? (y/n): ").strip().lower()
                    if action == "y":
                        ok, msg = engine.fire_employee(emp_id)
                        print(f"\n>> {msg}")
                else:
                    action = input(f"Нанять сотрудника {emp.name}? (y/n): ").strip().lower()
                    if action == "y":
                        ok, msg = engine.hire_employee(emp_id)
                        print(f"\n>> {msg}")

        elif choice == "4":
            print("\n--- УЛУЧШЕНИЯ МАГА3ИНА ---")
            for upg in engine.state.upgrades.values():
                status = "КУПЛЕНО" if upg.purchased else f"Цена: {upg.cost:.2f} ₽"
                print(f"[{upg.upg_id}] {upg.name} | {status} | {upg.description}")
            upg_id = input("\nВведите ID улучшения для покупки (или Enter для отмены): ").strip()
            if upg_id in engine.state.upgrades:
                ok, msg = engine.buy_upgrade(upg_id)
                print(f"\n>> {msg}")

        elif choice == "5":
            print("\n Проводим день в магазине...")
            summary = engine.simulate_day()
            print("\n" + "*" * 40)
            print(f" РЕЗУЛЬТАТЫ ДНЯ #{summary['day']}")
            print(f" Покупателей зашло: {summary['customers_count']}")
            print(f" Покупок совершено: {summary['items_sold']} шт. (Довольных: {summary['satisfied']}, Ушли без покупок: {summary['unsatisfied']})")
            print(f" Выручка: +{summary['revenue']:.2f} ₽")
            print(f" Зарплаты сотрудникам: -{summary['salaries']:.2f} ₽")
            if summary['theft_loss'] > 0:
                print(f" Убыток от краж: -{summary['theft_loss']:.2f} ₽")
            print(f" Чистая прибыль дня: {summary['net_profit']:.2f} ₽")
            if summary['event']:
                print(f" Событие дня: {summary['event']['title']} ({summary['event']['description']})")
            print("*" * 40)

        elif choice == "6":
            print("\n--- ИСТОРИЯ ФИНАНСОВ ---")
            if not engine.state.history:
                print("История пока пуста. Проведите хотя бы один день!")
            else:
                for log in engine.state.history[-10:]:
                    print(f"День {log['day']}: Выручка {log['revenue']:.2f} ₽ | Прибыль: {log['net_profit']:.2f} ₽ | Репутация: {log['reputation']:.1f}%")

        elif choice == "7":
            if engine.state.save_to_file():
                print("\n>> Игра успешно сохранена в savegame.json!")

        elif choice == "8":
            new_name = input("Введите новое название магазина: ").strip()
            if new_name:
                engine.state.shop_name = new_name
                print(f"\n>> Магазин переименован в '{new_name}'")

        elif choice == "0":
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    if "--cli" in sys.argv or not os.environ.get("DISPLAY"):
        run_cli()
    else:
        try:
            run_gui()
        except Exception as e:
            print(f"Ошибка запуска GUI: {e}, запуск CLI режима...")
            run_cli()
