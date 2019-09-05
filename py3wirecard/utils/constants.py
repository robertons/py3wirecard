# Define both API urls
BASE_URL_SANDBOX = 'https://sandbox.moip.com.br/v2/'
BASE_URL_LIVE = 'https://api.moip.com.br/v2/'

# Order constants
ORDER_URL = 'orders/'
ORDER_GET_URL = ORDER_URL + '{ORDER_ID}'

# Customer constants
CUSTOMER_URL = 'customers/'
CUSTOMER_GET_URL = CUSTOMER_URL + '{CUSTOMER_ID}'

# Payments constants
PAYMENT_URL = 'payments/'
PAYMENT_ORDER_URL = ORDER_URL + '{ORDER_ID}/payments'
PAYMENT_GET_URL = PAYMENT_URL + '{PAYMENT_ID}'
PAYMENT_CANCEL_URL= PAYMENT_URL + '{PAYMENT_ID}/void'

# Refunds constants
REFUND_URL = 'refunds/'
REFUND_ORDER_URL = ORDER_URL +'{ORDER_ID}/refunds'
REFUND_PAYMENT_URL = PAYMENT_URL + '{PAYMENT_ID}/refunds'
REFUND_GET_URL = REFUND_URL + '{REFUND_ID}'

# Notification constants
NOTIFICATION_URL = 'preferences/notifications/'
NOTIFICATION_GET_URL = NOTIFICATION_URL + '{NOTIFICATION_ID}'
REMOVE_NOTIFICATION_URL = NOTIFICATION_URL + '/{}'

# Webhooks constants
WEBHOOK_URL = 'webhooks'
WEBHOOK_GET_URL = WEBHOOK_URL + '?resourceId={RESOURCE_ID}'
