from PySide6.QtWidgets import (
    QWidget,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,

)

from app.ui.generated.ui_work_orders_page import Ui_WorkOrdersWindow
from app.services.work_order_service import WorkOrderService
from app.controllers.add_work_order_controller import AddWorkOrderController
from app.core.base_page import BasePage



class WorkOrdersPage(BasePage):


    def __init__(self):
        super().__init__()

        self.ui = Ui_WorkOrdersWindow()
        self.ui.setupUi(self)

        self.configure_table(
            self.ui.tblWorkOrders
        )

    def initialize_window(self):

        self.load_work_orders()

        self.ui.btnAdd.clicked.connect(self.add_work_order)
        self.ui.btnEdit.clicked.connect(self.edit_work_order)
        self.ui.btnDelete.clicked.connect(self.delete_work_order)
        self.ui.btnRefresh.clicked.connect(self.load_work_orders)
        self.ui.btnClose.clicked.connect(self.close)

        self.ui.txtSearch.textChanged.connect(self.search_work_orders)

    def load_work_orders(self):

        work_orders = WorkOrderService.get_work_orders()

        self.populate_table(work_orders)

    def populate_table(self, work_orders):

        self.ui.tblWorkOrders.setRowCount(len(work_orders))

        for row, work_order in enumerate(work_orders):

            for column, value in enumerate(work_order):

                self.ui.tblWorkOrders.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

        self.ui.tblWorkOrders.setColumnHidden(0, True)

        header = self.ui.tblWorkOrders.horizontalHeader()
        self.ui.tblWorkOrders.setSortingEnabled(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.lblStatus.setText(
            f"Showing {len(work_orders)} work orders"
        )

    def add_work_order(self):

        dialog = AddWorkOrderController()

        if dialog.exec():

            self.load_work_orders()

    def edit_work_order(self):

        row = self.ui.tblWorkOrders.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Select Work Order",
                "Please select a work order."
            )
            return
        
        work_order_id = int(
            self.ui.tblWorkOrders.item(row, 0).text()
        )

        dialog = AddWorkOrderController(work_order_id)

        if dialog.exec():

            self.load_work_orders()

    def delete_work_order(self):

        row = self.ui.tblWorkOrders.currentRow()

        if row < 0:

            QMessageBox.warning(
                self,
                "Select Work Order",
                "Please select a work order."
            )
            return
        
        work_order_id = int(
            self.ui.tblWorkOrders.item(row, 0).text()
        )

        reply = QMessageBox.question(
            self,
            "Delete",
            "Delete this work order?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:

            WorkOrderService.delete_work_order(work_order_id)

            self.load_work_orders()

    def search_work_orders(self):

        text = self.ui.txtSearch.text()

        if text:

            work_orders = WorkOrderService.search_work_order(text)

        else:

            work_orders = WorkOrderService.get_work_orders()

        self.populate_table(work_orders)