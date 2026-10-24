FROM odoo:17.0

USER root

# تثبيت الحزم البرمجية الأساسية لتشغيل أودو وربط الفاتورة الإلكترونية والمكتبات الرياضية للتنبؤ
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-pandas \
    python3-numpy \
    git \
    && rm -rf /var/lib/apt-get/lists/*

# تثبيت المكتبات عبر pip
RUN pip3 install --no-cache-dir \
    pytz \
    num2words \
    qrcode \
    requests

# إعداد صلاحيات مجلد الموديولات المخصصة والإعدادات
COPY ./config/odoo.conf /etc/odoo/
COPY ./custom_addons /mnt/extra-addons

RUN chown -R odoo:odoo /etc/odoo/odoo.conf /mnt/extra-addons

USER odoo

EXPOSE 8069 8072

CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]