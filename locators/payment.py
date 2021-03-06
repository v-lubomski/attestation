from selenium.webdriver.common.by import By


class PaymentLocators:
    BETWEEN_WALLETS = (By.ID, 'personal-payment')
    SMART_PAYMENT = (By.ID, 'smart-payment')
    DROPDOWN_VALUE = (By.XPATH, '/html/body/div[7]/ul/li[1]/div/span/strong')
    PAYMENT_DATE = (By.CLASS_NAME, 'day')
    PAYMENT_AMOUNT = (By.ID, 'amount')
    PAYMENT_COMMENT = (By.NAME, 'payment.comment')
    ALERT = (By.XPATH, '//*[@data-key="payment"]')
    FORWARD = (By.ID, 'forward')
    CARD_PAYMENTS = (By.ID, 'show-from-card-to-card-payment-form')
    CARD_PAYMENTS_AMOUNT = (By.NAME, 'payment.amount')
    CARD_PAYMENT_DEMO_ALERT = (By.XPATH, '//*[@data-key="payment.time"]')
    CARD_ERROR_ALERT = (By.CLASS_NAME, 'error-message')
    RECIPIENT_CARD = (By.NAME, 'payment.toCardId')
    PAYMENT_REQUEST_LINK = (By.XPATH, '//*[@id="dashboard-payment-type-menu"]/li[7]/a')
    PAYMENT_REQUEST_CARD = (By.NAME, 'cardPaymentRequest.cardId')
    PAYMENT_REQUEST_AMOUNT = (By.NAME, 'cardPaymentRequest.amount')
    PAYMENT_REQUEST_COMMENT = (By.NAME, 'cardPaymentRequest.details')
    PAYMENT_ALERT_SUCCESS = (By.XPATH, '//*[@id="alerts-container"]/div[1]')
    PAYMENT_PURPOSE = (By.XPATH, '//*[@id="payment-requests"]/tbody/tr[1]/td[3]')
    DATEPICKER = (By.XPATH, '//*[@class=" table-condensed"]')
    PAYMENT_REQUEST_POPUP = (By.ID, 'card-payment-request-dialog')
    PAYMENT_REQUEST_POPUP_CLOSE_BUTTON = (By.XPATH, '//*[@id="transaction-header"]//*[@class="close"]')
    PAYMENT_REQUEST = (By.XPATH, '//*[contains(@data-id, "10")]')
