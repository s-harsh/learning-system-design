# design Patterns: The "Mental Hook" Cheat Sheet 🧠

The secret to remembering patterns is **NOT** memorizing code. It is associating them with a **Physical Object** or **Pop Culture** reference.

Here is your "Lifetime Memory" list.

## 🏗️ Creational (How things are Born)

| Pattern | The "One Phrase" Hook | The Mental Image / Analogy |
| :--- | :--- | :--- |
| **Singleton** | *"There can be only one."* | **The Highlander** (or a Government President). Global access, strictly one instance. |
| **Factory** | *"You order, we decide."* | **Hring Manager**. You say "I need a Developer", the manager decides if they hire a Junior, Senior, or Intern. You just get a worker. |
| **Builder** | *"Step-by-step customization."* | **Subway Sandwich / LEGO**. You don't just "get a sandwich"; you say: "Bread -> Cheese -> Toasted -> Veggies". |

## 🔌 Structural (How things Look/Connect)

| Pattern | The "One Phrase" Hook | The Mental Image / Analogy |
| :--- | :--- | :--- |
| **Adapter** | *"Square peg, round hole."* | **Travel Plug Adapter**. US Plug (your code) -> Adapter -> UK Socket (legacy code). |
| **Decorator** | *"Wearing layers."* | **Iron Man Suit / Winter Jacket**. Tony Stark is the object. The Suit *decorates* him with flight and lasers. He is still Tony Stark inside. |
| **Facade** | *"One button to rule them all."* | **Car Start Button**. Pressing it triggers fuel injection, battery, spark plugs, starter motor... but you just press "START". |

## 🗣️ Behavioral (How things Talk/Act)

| Pattern | The "One Phrase" Hook | The Mental Image / Analogy |
| :--- | :--- | :--- |
| **Strategy** | *"Swappable Brains."* | **RPG Video Game Weapons**. You have an `Attack()` button. If you hold a **Sword**, it slashes. If you hold a **Bow**, it shoots. You swap the *Strategy* (Weapon) at runtime. |
| **Observer** | *"Don't call us, we'll call you."* | **YouTube Bell Icon / Magazine Sub**. When a new video drops, *everyone* who clicked the bell gets a ping. |
| **Command** | *"Order Ticket."* | **Restaurant Order Slip**. You (Client) give order to Waiter (Invoker). Waiter sticks it on the wall. Chef (Receiver) cooks it later. The order is now an *object* sitting on the wall. |
| **State** | *"Dr. Jekyll & Mr. Hyde."* | **The Hulk**. Bruce Banner behaves politely. When he gets angry (State Change), he behaves destructively. Same body, different state/behavior. |
| **Template** | *"Mad Libs / Form Filling."* | **A Legal Form**. The standard text is pre-written (Template). You just fill in the  `_______` (Blanks/Abstract Methods). |

---

### How to Practice
Next time you code:
1.  Need to connect two weird APIs? -> **"Where is my Travel Adapter?"** (Adapter)
2.  Need to process a list of items differently? -> **"I need to swap weapons."** (Strategy)
3.  Need to undo something? -> **"I need the restaurant ticket back."** (Command)
