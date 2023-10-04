class AuthRouter:
    """
    A database router to route authentication queries to the 'sign_up_pages_db' database.
    """

    def db_for_read(self, model, **hints):
        """
        All read operations should use the 'sign_up_pages_db' database.
        """
        if model._meta.app_label == 'auth':
            return 'sign_up_pages_db'
        return None

    def db_for_write(self, model, **hints):
        """
        All write operations should use the 'sign_up_pages_db' database.
        """
        if model._meta.app_label == 'auth':
            return 'sign_up_pages_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if both objects are in the 'auth' app.
        """
        if obj1._meta.app_label == 'auth' and obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations only for the 'auth' app to the 'sign_up_pages_db' database
        and specify the custom table for auth.User.
        """
        if app_label == 'auth':
            if model_name == 'User':
                return db == 'sign_up_pages_db' and model_name == 'sign_up_pages_user'
            else:
                return db == 'sign_up_pages_db'
        return None
