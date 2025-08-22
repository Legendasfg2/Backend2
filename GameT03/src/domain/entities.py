# src/domain/entities.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict
from enum import Enum


from ..config import MAX_INVENTORY_PER_TYPE


Position = Tuple[int, int]

class ItemKind(str, Enum):
 TREASURE = "treasure"
FOOD = "food"
POTION = "potion" # временный эффект (эльixir)
SCROLL = "scroll" # постоянный эффект
WEAPON = "weapon"




@dataclass
class Item:
 kind: ItemKind
subtype: str
hp: int = 0 # восстановление здоровья для еды
max_hp: int = 0 # прибавка к максимальному здоровью (scroll/potion)
agility: int = 0 # прибавка к ловкости
strength: int = 0 # прибавка к силе / оружие
cost: int = 0 # стоимость (для сокровищ)


def is_consumable(self) -> bool:
 return self.kind in {ItemKind.FOOD, ItemKind.POTION, ItemKind.SCROLL}




@dataclass
class Character:
id: int
name: str
max_hp: int
hp: int
agility: int
strength: int
weapon: Optional[Item] = None
pos: Position = (0, 0)


def is_alive(self) -> bool:
return self.hp > 0


def heal(self, amount: int) -> None:
if amount <= 0:
return
self.hp = min(self.max_hp, self.hp + amount)


def modify_max_hp(self, delta: int) -> None:
# изменение максимального здоровья. Если delta >0, одновременно увеличиваем текущее hp
return Player(id=player_id, name=name, max_hp=20, hp=20, agility=3, strength=3)