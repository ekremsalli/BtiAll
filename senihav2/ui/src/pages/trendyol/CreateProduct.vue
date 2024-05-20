<template>
  <q-page padding>
    <q-toolbar class="bg-grey-3 text-black">
      <q-toolbar-title>
        Ürün aktarımı
      </q-toolbar-title>
      <q-space />
      <q-btn @click="save()" flat dense>
        Kaydet
      </q-btn>
    </q-toolbar>

    <q-form ref="form" :disabled="!init" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false">
      <div class="row q-mt-sm">
        <div class="col-6">
          <div class="row">
            <div class="col">
              <q-select
                :disable="!init"
                dense
                outlined
                v-model="filters.product"
                label="Ürün *"
                use-input
                input-debounce="0"
                behavior="menu"
                :options="products"
                option-value="code"
                :option-label="(o) => `${o.name} (${o.code})`"
                emit-value
                map-options
                @input-value="search_product"
                @input="selected_product"
                :rules="[ val => val && val.length > 0 || 'Lütfen ürün seçin!']"
                reactive-rules
                >
              </q-select>
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model="record.barcode"
                label="Barkod *"
                :rules="[ val => val && val.length > 0 || 'Lütfen barkod belirtin!']"
                reactive-rules
                :disable="!selected" />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model="record.title"
                label="Ürün ismi *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val && val.length > 0 || 'Lütfen ürün ismi belirtin!']"
              />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model="record.product_main_code"
                label="Ana ürün kodu *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val && val.length > 0 || 'Lütfen ana ürün kodu belirtin!']"
              />
            </div>
          </div>

          <div class="row">
            <div class="col q-mt-sm">
              <q-select
                :disable="!selected"
                dense
                outlined
                v-model="filters.brand"
                label="Marka *"
                use-input
                input-debounce="0"
                behavior="menu"
                :options="brands"
                option-value="id"
                :option-label="(o) => `${o.name}`"
                emit-value
                map-options
                @input-value="search_brand"
                @input="selected_brand"
                :rules="[ val => check(val, 'marka') ]"
                reactive-rules
                >
              </q-select>
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model.number="record.quantity"
                label="Stok miktarı *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val !== null && isNaN(val) === false || 'Lütfen stok miktarı belirtin!']"
              />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model="record.stock_code"
                label="Stok kodu"
                :disable="!selected"
              />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model.number="record.dimensional_weight"
                label="Desi miktarı *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val !== null && isNaN(val) === false || 'Lütfen desi miktarı belirtin!']"
              />
            </div>
          </div>

          <div class="row q-mt-sm">
            <div class="col">
              <q-input
                dense
                v-model="record.currency_type"
                label="Para birimi *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val && val.length > 0 || 'Lütfen para birimi belirtin!']"
              />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model.number="record.list_price"
                label="Liste fiyatı *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val !== null && isNaN(val) === false || 'Lütfen liste fiyatı belirtin!']"
              />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model.number="record.sale_price"
                label="Satış fiyatı *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val !== null && isNaN(val) === false || 'Lütfen satış fiyatı belirtin!']"
              />
            </div>
          </div>

          <div class="row">
            <div class="col">
              <q-input
                dense
                v-model.number="record.vat_rate"
                label="KDV oranı *"
                :disable="!selected"
                reactive-rules
                :rules="[ val => val !== null && isNaN(val) === false || 'Lütfen desi miktarı belirtin!']"
              />
            </div>
          </div>

          <div class="row q-mt-sm">
            <div class="col">
              <q-select
                :disable="!selected"
                dense
                outlined
                v-model="cargo_company"
                label="Kargo firması *"
                :options="cargos"
                option-value="id"
                :option-label="(o) => `${o.name} (${o.taxNumber})`"
                :rules="[ val => check(val, 'kargo') ]"
                reactive-rules
                >
              </q-select>
            </div>
          </div>
        </div>

        <div class="col-6">
          <div class="row">
            <div class="col q-ml-md">
               <q-editor
                placeholder="Ürün açıklaması"
                :disable="!selected"
                v-model="editor"
                :rules="[ val => val && val.length > 0 || 'Lütfen açıklama belirtin!']"
                min-height="14rem" />
             </div>
          </div>

          <div class="row">
            <div class="col q-ml-md q-mt-sm">
              <q-input @keyup.enter="add_img" bottom-slots dense v-model="url" label="Resim URL" :disable="!selected || images.length > 7">
                <template #append>
                  <q-icon name="add" @click.stop="add_img" class="cursor-pointer" />
                </template>

                <template #hint>
                  Görsel url adresi (Adresler SSL sertifikalı "https" formatında adresler olmalıdır)
                </template>
              </q-input>
              <q-img
                class="q-ma-xs"
                @click='remove_image(index)'
                :key="index"
                v-for="(image, index) in images"
                :src="image"
                style="max-width: 60px; curor:pointer; border: 1px dotted red;min-height:60px" />
            </div>
          </div>

          <q-separator class="q-ml-md text-black" />
          <div class="row">
            <div class="col q-ml-md q-my-sm q-pb-md">
              <q-select
                ref="cat"
                :disable="!selected"
                dense
                outlined
                v-model="cat"
                option-value="id"
                :option-label="(o) => `${o.name}`"
                :options="cats"
                @input="find_subs"
                bottom-slots
                :rules="[ val => check(val, 'kategori') ]"
                reactive-rules
                label="Kategori *">
                <template #append>
                  <q-icon name="close" @click.stop="clear_cat" class="cursor-pointer" />
                </template>

                <template #hint>
                  <span class='text-negative' v-if="cat && cat.subCategories.length > 0"> * En alt kategoriye kadar seçim yapmalısınız.<br /></span>
                  {{ parent_cats }}
                </template>
              </q-select>
            </div>
          </div>

          <div class="row">
            <div class="col q-ml-md q-mt-sm">
              <span class="text-body2">Özellikler</span>
              <template v-for="attr in attrs">
                <AttrInput v-model="avals[attr.attribute.id]" v-if="attr.required" :attr="attr" :key="attr.attribute.id" />
              </template>
            </div>
          </div>


        </div>
      </div>
    </q-form>
  </q-page>
</template>

<script>
  import Service from 'boot/service'
  import { common } from 'src/mixins/common'
  import treeSearch  from 'tree-search'
  const find = treeSearch('subCategories')
  import AttrInput from 'components/AttrInput'

  export default {
    name: 'CreateProduct',
    mixins: [common],
    components: {
      AttrInput
    },
    computed: {
      parent_cats() {
        return this.roots.map(o => o.name).join(' > ')
      },
      cats () {
        if (this.roots.length > 0){
          let root = this.roots[this.roots.length - 1]
          if (root.subCategories && root.subCategories.length > 0) return root.subCategories
          else {
            let fin = this.roots.filter(o => o.id == this.cat.parentId).shift()
            if (fin) return fin.subCategories
          }
        } else return this.categories
      },
    },
    data() {
      return {
        filters: {product: null, brand: null},
        products: [],
        init: false,
        selected: null,
        record: {},
        brands: [],
        categories: [],
        cargos: [],
        roots: [],
        cat: null,
        editor: '',
        images: [],
        url: "",
        attrs: [],
        avals: {},
        cargo_company: null
      }
    },
    mounted() {
      this.initialize({})

      // remove before release
      /*
      this.record = {
        'sale_price': 80,
        'list_price': 100,
        'dimensional_weight': 0,
        'currency_type': 'TL',
        'quantity': 0
      }
      this.images = [
        'https://homepages.cae.wisc.edu/~ece533/images/airplane.png'
      ]
      */
    },
    methods: {
      remove_image(index) {
        this.$delete(this.images, index)
      },
      check(val, msg){
        if (val === null) return `Lütfen ${msg} belirtin`
        return true
      },
      save() {
        const self = this
        // validasyon ve ürünün oluşturulması!
        this.$refs.form.validate().then(success => {
          if (success){
            // en az bir resim eklenmiş mi?
            if (!self.editor || self.editor.length == 0) {
              this.um('Lütfen ürün açıklamasını belirtin!')
              return
            }
            if (self.cat && self.cat.subCategories.length > 0) {
              this.um('Lütfen en alt kategoriye kadar seçim yapın!')
              return
            }
            if (self.images && self.images.length == 0){
              this.um('Lütfen en az bir resim ekleyin!')
              return
            }
            if (!self.cargo_company || self.cargo_company == null) {
              this.um('Lütfen kargo firması belirtin!')
              return
            }
            let attrs = []
            for (const [key,value] of Object.entries(self.avals)){
              if (typeof value === 'object' && value !== null){
                attrs.push({
                  attributeId: key,
                  attributeValueId: value.id
                })
              } else {
                attrs.push({
                  attributeId: key,
                  customAttributeValue: value
                })
              }
            }
            let images = []
            self.images.forEach(function(item){
              images.push({url: item})
            })
            let record = this.record
            let data = {
              'barcode': record.barcode,
              'title': record.title,
              'product_main_id': record.product_main_code,
              'brand_id': record.brand_id,
              'category_id': self.cat ? self.cat.id : 0,
              'quantity': record.quantity,
              'stock_code': record.stock_code ? record.stock_code : '',
              'dimensional_weight': record.dimensional_weight,
              'description': self.editor,
              'currency_type': record.currency_type,
              'list_price': record.list_price,
              'sale_price': record.sale_price,
              'cargo_company_id': self.cargo_company ? self.cargo_company.id : 0,
              'images':  images,
              'vat_rate': record.vat_rate,
              'attributes': attrs
            }
            Service.post('trendyol/product', data)
              .then((response) => {
                console.log(response)
                let transfer = response.data.transfer
                if (transfer && transfer.batchRequestId){
                  self.bm(`Ürün ${transfer.batchRequestId} istek numarası ile başarıyla aktarıldı!`)
                  self.$router.push({name: 'trendyol/urunler'})
                }
              })
              .catch((error) => {
                self.um('Bir hata oluştu!' + error)
              })
          }
        })

      },
      add_img() {
        if (this.url.startsWith('https://')){
          if (this.images.includes(this.url)){
            this.um('Bu resim listede mevcut!')
          } else {
            this.images.push(this.url)
            this.$set(this, "url", "")
          }
        } else {
          this.um('URL https:// ile başlamalı!')
        }
      },
      clear_cat() {
        this.$set(this, "roots", [])
        this.$set(this, "cat", null)
        this.$set(this, "attrs", [])
        this.$set(this, "avals", {})
      },
      find_subs(val) {
        if (this.roots.length > 0) {
          let last = this.roots[this.roots.length - 1]
          if (last.id == val.parentId) {
            this.roots.push(val)
            if (this.$refs.cat && val.subCategories.length > 0) this.$refs.cat.showPopup()
            else this.get_attrs(val)
          }
          else {
            this.roots.pop()
            this.roots.push(val)
            this.get_attrs(val)
          }
        } else {
          this.roots.push(val)
          if (this.$refs.cat) this.$refs.cat.showPopup()
        }
      },
      get_attrs(val) {
        const self = this
        Service.get('trendyol/attrs', { params: { id: val.id }})
          .then((response) => {
            self.$set(self, "attrs", response.data.attrs.categoryAttributes || {})
            self.$set(self, "avals", {})
          })
          .catch((error) => {
            this.um('Bir hata oluştu!' + error)
          })
      },
      initialize(params) {
        const self = this
        this.$set(this, "init", false)
        Service.get('trendyol/init', { params: params })
          .then((response) => {
            self.$set(self, "categories", response.data.categories.categories)
            self.$set(self, "cargos", response.data.cargos)
            self.$set(self, "products", response.data.items)
            self.$set(self, "brands", response.data.brands.brands)
            self.$set(self, "init", true)
            Object.freeze(self.categories)
          })
          .catch((error) => {
            if (error.response) {
              if (error.response.data.description) this.um(error.response.data.description)
              else this.um('Bir hata oluştu! ' + error.response.data)
            } else this.um('Bilinmeyen hata oluştu!')
          })
      },
      filter_func (val, update) {
        if (val === '') {
          update(() => {
            this.options = stringOptions
          })
          return
        }
        update(() => {
          const needle = val.toLowerCase()
          this.options = stringOptions.filter(v => v.toLowerCase().indexOf(needle) > -1)
        })
      },
      selected_product() {
        const self = this
        this.$set(this, "selected", this.filters.product)
        Service.get('product/detail', { params: { code: this.filters.product }})
          .then((response) => {
            self.selected = response.data.product
            if (response.data.barcode) {
              self.$set(self.record, "barcode", response.data.barcode)
            } else {
            }
            self.$set(self.record, "title", self.selected.name)
            self.$set(self.record, "product_main_code", self.selected.code)
            self.$set(self.record, "vat_rate", self.selected.vat)
          })
          .catch((error) => {
            this.um('Bir hata oluştu! ' + error)
          })
      },
      search_product(val) {
        const self = this
        if (val.length === 0) return
        Service.get('product/search', { params: { name__icontains: val }})
          .then((response) => {
            self.products = response.data.results
          })
          .catch((error) => {
            this.um('Bir hata oluştu!' + error)
          })
      },
      selected_brand(){
        const self = this
        this.$set(this.record, "brand_id", this.filters.brand)
      },
      search_brand(val) {
        const self = this
        if (val.length === 0) return
        Service.get('trendyol/brand', { params: { val: val }})
          .then((response) => {
            self.brands = response.data.brands
          })
          .catch((error) => {
            this.um('Bir hata oluştu!' + error)
          })
      }
    }
  }
</script>

<style lang="css">
</style>
