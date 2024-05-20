<template>
  <q-card>
    <div class="row">
      <div class="col-5">
        <q-list>
          <q-item>
            <q-item-section>
              <q-item-label>Sipariş numarası</q-item-label>
              <q-item-label caption>{{ item.orderNumber }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <q-item-label>Sipariş tarihi</q-item-label>
              <q-item-label caption>{{ orderDate }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <q-item-label>Kişi</q-item-label>
              <q-item-label caption>{{ item.customerFirstName }} {{ item.customerLastName }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <q-item-label>Fatura adresi</q-item-label>
              <q-item-label caption>
                {{ item.invoiceAddress.fullAddress }} ({{ item.invoiceAddress.fullName }})
              </q-item-label>
            </q-item-section>
          </q-item>

          <q-item v-if="item.invoiceAddress.fullAddress != item.shipmentAddress.fullAddress">
            <q-item-section>
              <q-item-label>Sevkiyat adresi</q-item-label>
              <q-item-label caption>
                {{ item.shipmentAddress.fullAddress }} ({{ item.shipmentAddress.fullName }})
              </q-item-label>
            </q-item-section>
          </q-item>

          <q-item>
            <q-item-section>
              <q-item-label>Kargo</q-item-label>
              <q-item-label caption>
                {{ item.cargoProviderName }} ({{ item.cargoTrackingNumber }})
              </q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </div>
      <div class="col-7">
        <q-table dense :data="item.lines" :columns="cols">
          <template #body-cell-barcode="props">
            <q-td :props="props">
              {{ props.row.barcode }}
              <q-tooltip>
                <strong>ID: </strong> {{ props.row.id }}<br />
                <strong>Ürün kodu:</strong> {{ props.row.productCode }}<br />
                <strong>Ürün adı:</strong> {{ props.row.productName }}<br />
                <strong>KDV oranı: </strong> {{ props.row.vatBaseAmount }} <br />
                <strong>Satış kampanya no: </strong> {{ props.row.salesCampaignId }}
              </q-tooltip>
            </q-td>
          </template>

          <template #body-cell-total="props">
            <q-td :props="props">
              {{ props.row.amount }} {{ props.row.currencyCode }}
            </q-td>
          </template>

        </q-table>
      </div>
    </div>
  </q-card>
</template>

<script>
  import { date } from 'quasar'
  export default {
    props: {
      item: {
        type: Object,
        required: true
      },
      log: {
        type: Object,
        required: false
      }
    },
    computed: {
      orderDate () {
        return date.formatDate(
          date.subtractFromDate(
            this.item.orderDate, {hours: 0}), 'DD MMMM YYYY HH:mm')
      }
    },
    data() {
      return {
        cols: [
          { field: 'barcode', label: 'Barkod', name: 'barcode', sortable: false, align: 'left' },
          { field: 'total', label: 'Tutar', name: 'total', sortable: false, align: 'left' },
          { field: 'quantity', label: 'Adet', name: 'quantity', sortable: false, align: 'left' }
        ]
      }
    },
  }
</script>