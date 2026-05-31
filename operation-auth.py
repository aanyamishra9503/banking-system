import hashlib
   def hash_password(password):
        return hashlib.sha256(password.encode(*).hexdigest()

   def verify_password(input_pass, stored_hash):
        return hash_password(input_pass)== stored_hash