class MenuHandler:
    @staticmethod
    def display_menu(title, options):
        """Hiển thị menu với tiêu đề và các lựa chọn"""
        print("\n" + "="*50)
        print(f"{title:^50}")
        print("="*50)
        for key, value in options.items():
            print(f"{key}. {value}")
        print("="*50)

    @staticmethod
    def get_choice(prompt):
        """Lấy lựa chọn từ người dùng"""
        return input(prompt).strip()

    @staticmethod
    def handle_menu(title, options, handlers):
        """Xử lý menu và các lựa chọn của người dùng"""
        while True:
            MenuHandler.display_menu(title, options)
            choice = MenuHandler.get_choice("Nhập lựa chọn của bạn: ")
            
            if choice == '0':
                break
                
            if choice in handlers:
                handlers[choice]()
            else:
                print("Lựa chọn không hợp lệ!")
                
            input("\nNhấn Enter để tiếp tục...") 