class WalletSystem:
def **init**(self): # Initialize your storage here
pass

    def credit(self, user_id, amount, idempotency_key):
        # Your logic here
        pass

    def debit(self, user_id, amount, idempotency_key):
        # Your logic here
        pass

    def get_balance(self, user_id):
        # Your logic here
        pass

```

**Which one feels more comfortable to you?** Pick one and stick with it.

---

## 🤔 Step 3: The `get_balance` Function (Start Here - Easiest!)

**This is the simplest function. Let's think through it:**

**What does it do?**
- Takes a `user_id`
- Returns the balance for that user

**Questions to think about:**
1. Where is the balance stored? (Your dictionary from Step 1)
2. How do I get a value from a dictionary? (Syntax: `dict[key]`)
3. What if the user doesn't exist yet? (What should you return? 0? Error?)

**Decision to make:** Do you return 0 for unknown users, or raise an error?
- Option 1: Return 0 (simpler, "implicit creation")
- Option 2: Return error (more explicit)

**The problem says:** "Decide how to handle unknown users and explain your choice"

**What would YOU choose and why?**

**Try writing this function yourself now. Just this one. Take 10 minutes.**

---

## 🤔 Step 4: The `credit` Function (Medium difficulty)

**What does it do?**
- Adds money to a user's balance
- But only if this exact operation hasn't happened before (idempotency)

**Step-by-step thinking:**

1. **Validate amount:** Is it positive?
   - If not: What do you do? (Return error? Raise exception?)

2. **Check idempotency:** Has this `idempotency_key` been used before?
   - Where do you check? (The operations dictionary from Step 1)
   - If yes: What do you do? (Skip operation, return current balance)

3. **Add money:**
   - Get current balance (might be 0 if new user)
   - Add the amount
   - Update the dictionary

4. **Record operation:**
   - Mark this idempotency_key as "used"
   - What do you store? (Maybe the amount? Or just True?)

**Questions for you:**
1. How do you check if a key exists in a dictionary? (Hint: `in` keyword)
2. How do you add to a number? (Hint: `+=` or `= old_value + amount`)
3. How do you add a new key to a dictionary? (Hint: `dict[key] = value`)

**Try writing pseudocode first:**
```

function credit: 1. Check if amount is positive - If not: return error

    2. Check if idempotency_key was already used
       - If yes: return current balance (don't credit again)

    3. Get current balance (or 0 if new user)

    4. Add amount to balance

    5. Save new balance

    6. Mark idempotency_key as used

    7. Return new balance
