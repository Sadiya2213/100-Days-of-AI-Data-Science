
raw_shopping_cart = ["iPhone 16", "AirPods", "iPhone 16", "MacBook Pro", "AirPods", "Spam_Link_XYZ"]

print("🛒 --- Raw Shopping Cart Data ---")
print(raw_shopping_cart)


unique_cart = set(raw_shopping_cart)
print(f"\n✨ Cleaned Unique Items (Set): {unique_cart}")


spam_keywords = {"Spam_Link_XYZ", "Malicious_Ad_01"}


final_verified_cart = unique_cart.difference(spam_keywords)
print(f"🔒 Final Verified Cart (Spam Removed): {final_verified_cart}\n")


if len(final_verified_cart) == 0:
    print("⚠️ Warning: Your cart is empty or contained only spam items.")
else:
    print(f"✅ Success! You have {len(final_verified_cart)} valid items ready for checkout.")
    
    
    if "iPhone 16" in final_verified_cart:
        print("📱 Note: Premium electronics detected in cart. Applying student discount code!")
