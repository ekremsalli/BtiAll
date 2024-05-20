<template>
  <div>
    <q-page padding>
      <q-toolbar class="bg-grey-3 text-black">
        <q-toolbar-title>
          <span class="text-red-7">Operasyon Kodları</span>
        </q-toolbar-title>

        <q-space />

        <q-btn
          :loading="loading"
          @click="refresh()"
          flat
          round
          dense
          icon="fas fa-sync-alt"
          class="q-mr-sm"
        >
          <q-tooltip>
            Yenile
          </q-tooltip>
        </q-btn>

        <q-select
          v-model="visible"
          multiple
          outlined
          dense
          options-dense
          :display-value="$q.lang.table.columns"
          emit-value
          map-options
          :options="cols"
          option-value="name"
          options-cover
          style="min-width: 150px"
        >
        </q-select>
      </q-toolbar>

      <q-table
        :data="data"
        :columns="cols"
        row-key="id"
        :pagination.sync="pagination"
        :loading="loading"
        binary-state-sort
        :visible-columns="visible"
        no-data-label="Kayıt bulunamadı!"
        :rows-per-page-options="[]"
        @request="load"
      >
        <template v-slot:top>
          <q-space />
          <q-btn @click="create_op_dialog = true" color="dark" label="Yeni Oluştur" />
        </template>

        <template v-slot:body-cell-code="props">
          <q-td :props="props">
            <span
              @click="detail_dialog_func(props.row)"
              style="cursor: pointer"
              >{{ props.row.code }}</span
            >
          </q-td>
        </template>

        <template v-slot:body-cell-ops="props">
          <q-td :props="props">
            <q-btn
              @click="detail_dialog_func(props.row)"
              push
              color="light-blue-6"
              label="Detay"
              size="sm"
              class="q-mr-sm"
            />
            <q-btn
              @click="op_dialog_func(props.row)"
              push
              color="blue-grey-6"
              icon="edit"
              size="sm"
              class="q-mr-sm"
            />
            <q-btn
              @click="op_delete(props.row)"
              push
              color="red-5"
              icon="delete"
              size="sm"
              class="q-mr-sm"
            />
          </q-td>
        </template>
      </q-table>
    </q-page>

    <!-- New creating operation code dialog -->
    <q-dialog v-model="create_op_dialog">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Operasyon Oluştur</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <div>
            <q-input
              dense
              v-model="filter.op"
              label="Operasyon Kodu"
              class="q-mt-md"
              autofocus
              @keyup.esc="create_op_dialog = false"
            />
          </div>

          <div>
            <q-input
              dense
              v-model="filter.description"
              label="Operasyon Açıklaması"
              class="q-mt-md"
              autofocus
              @keyup.esc="create_op_dialog = false"
            />
          </div>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="İptal" v-close-popup />
          <q-btn :disable="filter.op && filter.op.trim() && filter.description && filter.description.trim() ? false : true " @click="op_create" color="dark" label="Yeni Oluştur" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <!-- Operation code edit dialog -->
    <q-dialog v-model="op_dialog">
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Operasyon Kodu</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input
            dense
            label="Operasyon Kodu"
            v-model="record.code"
            @keyup.esc="op_dialog = false"
          />

          <q-input
            dense
            v-model="record.description"
            label="Operasyon Açıklaması"
            @keyup.esc="op_dialog = false"
          />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="İptal" v-close-popup />
          <q-btn flat label="Güncelle" :disable="record.code && record.code.trim() && record.description && record.description.trim() ? false : true " @click="op_update" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>

    <!-- Operation Dialog Start -->
    <q-dialog
      v-model="dialog"
      persistent
      :maximized="maximizedToggle"
      transition-show="slide-up"
      transition-hide="slide-down"
    >
      <q-card class="bg-blue-grey-4 text-white">
        <q-bar>
          <q-space />

          <q-btn
            dense
            flat
            icon="minimize"
            @click="maximizedToggle = false"
            :disable="!maximizedToggle"
          >
            <q-tooltip v-if="maximizedToggle" class="bg-white text-primary"
              >Küçült</q-tooltip
            >
          </q-btn>
          <q-btn
            dense
            flat
            icon="crop_square"
            @click="maximizedToggle = true"
            :disable="maximizedToggle"
          >
            <q-tooltip v-if="!maximizedToggle" class="bg-white text-primary"
              >Büyült</q-tooltip
            >
          </q-btn>
          <q-btn dense flat icon="close" v-close-popup>
            <q-tooltip class="bg-white text-primary">Kapat</q-tooltip>
          </q-btn>
        </q-bar>

        <q-card-section>
          <div class="text-h6">Operasyon</div>
        </q-card-section>
        <template v-if="active">
          <q-card-section class="q-pt-none">
            <!-- Operation Dialog Table Start -->
            <q-toolbar class="bg-grey-3 text-black">
              <q-toolbar-title>
                <div :class="active.description ? 'q-mt-sm' : 'q-mt-none'">
                  <span class="text-red-5 text-bold">{{ active.code }}</span> koda
                ait tablolar listelenmiştir.
                <br />
                <span class="text-subtitle1">{{ active.description }}</span> 
                </div>
              </q-toolbar-title>
              

              <q-space />

              <q-btn
                :loading="loading"
                @click="refresh()"
                flat
                round
                dense
                icon="fas fa-sync-alt"
                class="q-mr-sm"
              >
                <q-tooltip>
                  Yenile
                </q-tooltip>
              </q-btn>

              <q-select
                v-model="visible"
                multiple
                outlined
                dense
                options-dense
                :display-value="$q.lang.table.columns"
                emit-value
                map-options
                :options="cols"
                option-value="name"
                options-cover
                style="min-width: 150px"
              >
              </q-select>
            </q-toolbar>

            <q-table
              :data="active.details"
              :columns="dialog_cols"
              row-key="id"
              :loading="dialog_loading"
              :visible-columns="dialog_cols_visible"
              no-data-label="Kayıt bulunamadı!"
              class="q-mt-sm"
            >
              <template v-slot:top>
                <q-btn
                  @click="op_detail_add_dialog_func"
                  color="light-blue-6"
                  label="Yeni Kayıt Ekle"
                  push
                />
              </template>

              <template v-slot:body-cell-is_debit="props">
                <q-td :props="props">
                  {{ props.row.is_debit ? "Borçlu" : "Alacaklı" }}
                </q-td>
              </template>

              <template v-slot:body-cell-ops="props">
                <q-td :props="props">
                  <q-btn
                    @click="op_detail_update_dialog(props.row)"
                    color="light-blue-6"
                    label="Güncelle"
                    push
                  />
                  <q-btn
                    @click="op_detail_delete(props.row.id)"
                    color="red-5"
                    label="Sil"
                    push
                    class="q-ml-sm"
                  />
                </q-td>
              </template>
            </q-table>
          </q-card-section>

          <q-dialog v-model="op_detail_dialog">
            <q-card style="min-width:500px">
              <q-card-section>
                <div class="text-h6">Güncelle</div>
              </q-card-section>

              <q-separator />

              <q-card-section style="max-height: 50vh" class="scroll">
                <div class="row">
                  <div class="col-md-6">
                    <q-input v-model="record.field" label="Hesap Adı" filled />
                  </div>

                  <div class="col-md-6">
                    <q-input
                      v-model="record.account"
                      label="Hesap Kodu"
                      filled
                    />
                  </div>
                </div>
                <div class="row q-mt-sm">
                  <div class="col-md-6">
                    <q-select
                      v-model="record.is_debit"
                      :options="is_debits"
                      :option-value="o => o.id"
                      :option-label="o => o.title"
                      map-options
                      emit-value
                      label="Borç/Alacak"
                      filled
                    />
                  </div>

                  <div class="col-md-6">
                    <q-input v-model="record.formula" label="Formül" filled />
                  </div>
                </div>
              </q-card-section>

              <q-separator />

              <q-card-actions align="right">
                <q-btn flat label="İptal" color="red-3" v-close-popup />
                <q-btn
                  flat
                  label="Güncelle"
                  color="primary"
                  @click="op_detail_update"
                  v-close-popup
                />
              </q-card-actions>
            </q-card>
          </q-dialog>

          <q-dialog v-model="op_detail_add_dialog">
            <q-card style="min-width:500px">
              <q-card-section>
                <div class="text-h6">Yeni Kayıt Ekle</div>
              </q-card-section>

              <q-separator />

              <q-card-section style="max-height: 50vh;" class="scroll">
                <div class="row justify-around">
                  <div class="col-6">
                    <q-select
                      filled
                      map-options
                      emit-value
                      :options="fields"
                      v-model="adding.field"
                      label="Hesap Adı"
                      filled
                      :rules="[
                        val => (val && val.trim() && val.length >= 0) || 'Bu alan zorunludur'
                      ]"
                    />
                  </div>

                  <div class="col-6 q-pl-sm">
                    <q-input
                      v-model="adding.account"
                      label="Hesap Kodu"
                      filled
                      :rules="[
                        val => (val && val.trim() &&  val.length >= 0) || 'Bu alan zorunludur'
                      ]"
                    />
                  </div>
                </div>
                <div class="row q-mt-sm justify-around">
                  <div class="col-6">
                    <q-select
                      v-model="adding.is_debit"
                      :options="is_debits"
                      option-value="id"
                      option-label="title"
                      map-options
                      emit-value
                      label="Borç/Alacak"
                      filled
                    />
                  </div>

                  <div class="col-6 q-pl-sm">
                    <q-input
                      v-model="adding.formula"
                      label="Formül"
                      prefix="ƒ(n)"
                      filled
                    />
                  </div>
                </div>
              </q-card-section>

              <q-separator />

              <q-card-actions align="right">
                <q-btn push label="İptal" color="red-5" v-close-popup />
                <q-space />
                <q-btn
                  :disable="adding.field && adding.account ? false : true"
                  push
                  label="Ekle"
                  color="light-blue-6"
                  @click="op_detail_new_add"
                  v-close-popup
                />
              </q-card-actions>
            </q-card>
          </q-dialog>
        </template>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import Service from "boot/service";
import { common } from "src/mixins/common";
import { date } from "quasar";
import AddOperationCode from "../../components/AddOperationCode.vue";

export default {
  name: "mp_operation",
  components: {
    AddOperationCode
  },
  mixins: [common],
  data() {
    return {
      loading: false,
      dialog_loading: false,
      data: [],
      cols: [
        {
          field: "id",
          label: "ID",
          name: "id",
          sortable: true,
          align: "left"
        },

        {
          field: "code",
          label: "Operasyon Kodu",
          name: "code",
          sortable: true,
          align: "left"
        },
        {
          field: "description",
          label: "Açıklama",
          name: "description",
          sortable: false,
          align: "left"
        },
        {
          field: "created",
          label: "Oluşturulma Tarihi",
          name: "created",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY")
        },
        {
          field: "ops",
          label: "İşlemler",
          name: "ops",
          sortable: false,
          align: "right"
        }
      ],
      visible: ["code", "description", "created", "ops"],

      dialog_cols: [
        {
          field: "id",
          label: "ID",
          name: "id",
          sortable: true,
          align: "left"
        },

        {
          field: "field",
          label: "Hesap Adı",
          name: "field",
          sortable: true,
          align: "left"
        },
        {
          field: "account",
          label: "Hesap Kodu",
          name: "account",
          sortable: true,
          align: "left"
        },
        {
          field: "is_debit",
          label: "Borç - Alacak",
          name: "is_debit",
          sortable: true,
          align: "left"
        },
        {
          field: "formula",
          label: "Kullanılan Formül",
          name: "formula",
          sortable: false,
          align: "left"
        },
        {
          field: "created",
          label: "Oluşturulma Tarihi",
          name: "created",
          sortable: true,
          align: "left",
          format: (val, row) => date.formatDate(val, "DD/MM/YY")
        },
        {
          field: "ops",
          label: "İşlemler",
          name: "ops",
          sortable: false,
          align: "right"
        }
      ],
      dialog_cols_visible: [
        "field",
        "account",
        "is_debit",
        "formula",
        "created",
        "operation",
        "ops"
      ],
      pagination: {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 10,
        rowsNumber: 10
      },
      dialog_pagination: {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 10,
        rowsNumber: 10
      },
      filter: {},
      dialog: false,
      maximizedToggle: true,
      active: null,
      op_dialog: false,
      create_op_dialog: false,
      op_detail_dialog: false,
      record: {},
      is_debits: [
        {
          id: "true",
          title: "Borçlu"
        },
        {
          id: "false",
          title: "Alacaklı"
        }
      ],
      is_debit: null,
      op_detail_add_dialog: false,
      adding: {},
      fields: ['amount', 'total_amount', 'commission_amount']
    };
  },
  mounted() {
    this.load({ pagination: this.pagination });
  },
  methods: {
    refresh() {
      this.$set(this, "pagination", {
        sortBy: "desc",
        descending: false,
        page: 1,
        rowsPerPage: 3,
        rowsNumber: 10
      });
      this.load({ pagination: this.pagination });
    },
    load(sett) {
      let self = this;
      this.$set(this, "loading", true);
      this.$set(this, "data", []);
      const params = {
        page: sett.pagination.page,
        page_size: sett.pagination.rowsPerPage,
        ordering: sett.pagination.descending
          ? "-" + sett.pagination.sortBy
          : sett.pagination.sortBy
      };

      Service.get("/app/v1/op", params)
        .then(response => {
          self.$set(self, "data", response.data.results);

          self.pagination.rowsNumber = response.data.total;
          self.pagination.page = response.data.current;
          self.pagination.rowsPerPage = response.data.page_size;
          self.pagination.descending = response.data.descending;
          self.pagination.sortBy = response.data.ordering;
        })
        .catch(error => {
          self.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          self.$set(this, "loading", false);
        });
    },

    dialog_load(sett) {},

    op_create() {
      let self = this;
      let params = {
        code: self.filter.op,
        description: self.filter.description
      };
      Service.post(`/app/v1/op`, params)
        .then(response => {
          self.bm("Operasyon kodu oluşturuldu.");
          self.$set(self.filter, 'op', null)
          self.$set(self.filter, 'description', null)
          
          self.data.push(response.data);
        })
        .catch(error => {
          self.um("Bir hata oluştu!" + error);
        })
        .finally(() => {
          self.$set(this, "loading", false);
        });
    },

    op_dialog_func(active) {
      this.$set(this, "op_dialog", true);
      this.$set(this.record, "code", active.code);
      this.$set(this.record, "description", active.description);
      this.$set(this, "active", active);
    },

    op_update() {
      let self = this;

      Service.patch(`/app/v1/op/${self.active.id}`, this.record)
        .then(response => {
          self.bm("Operasyon kodu güncellendi.");
          let dx;
          self.data.forEach((val, index) => {
            if (val.id === self.active.id) dx = index;
          });

          if (dx !== undefined) {
            self.data.splice(dx, 1);
            self.data.insert(dx, response.data);
          }
        })
        .catch(err => {
          self.um("Operasyon kodunu güncellerken bir hata oluştu!" + err);
        });
    },

    op_delete(row) {
      let self = this;
      if (row.details && row.details.length > 0) {
        self.uy(
          "Bu operasyon kodunun içerisinde alt öğeler yer aldığından dolayı silinememektedir. Lütfen ilk önce alt öğeleri siliniz."
        );

        return
      }

      Service.delete(`/app/v1/op/${row.id}`)
        .then(response => {
          self.bm("Operasyon kodu silindi.");
          let dx;
          self.data.forEach((val, index) => {
            if (val.id === row.id) dx = index;
          });

          if (dx !== undefined) {
            self.data.splice(dx, 1);
          }
        })
        .catch(err => {
          self.um("Operasyon kodu silinirken bir hata oluştu" + err);
        });
    },

    detail_dialog_func(row) {
      let self = this;

      self.$set(self, "active", row);
      self.$set(self, "dialog", true);
    },

    op_detail_create() {
      let self = this;
      let params = {
        field: self.adding.field,
        account: self.adding.account,
        operation: self.adding.operation
      };
      if (self.adding.is_debit) params["is_debit"] = self.adding.is_debit;
      if (self.adding.formula) params["formula"] = self.adding.formula;

      Service.post("/app/v1/op/detail", params)
        .then(response => {
          self.bm("Yeni kayıt eklendi.");
          self.data.push(response.data);
        })
        .catch(err => {
          self.um("Yeni kayıt eklenirken bir hata oluştu!" + err);
        });
    },

    op_detail_update_dialog(row) {
      let self = this;
      self.op_detail_dialog = true;

      self.$set(this, "record", {
        id: row.id,
        account: row.account,
        field: row.field,
        formula: row.formula,
        is_debit: row.is_debit ? "true" : "false"
      });
    },

    op_detail_update() {
      let self = this;

      Service.patch(`/app/v1/op/detail/${self.record.id}`, self.record)
        .then(response => {
          self.bm("Başarıyla güncellendi");

          let dx;
          self.active.details.forEach((val, index) => {
            if (val.id === self.record.id) dx = index;
          });

          if (dx !== undefined) {
            self.active.details.splice(dx, 1);
            self.active.details.insert(dx, response.data);
          }
        })
        .catch(err => {
          self.um("Güncellerken hata oluştu" + err);
        });
    },

    op_detail_add_dialog_func() {
      this.op_detail_add_dialog = true;
      this.$set(this, "adding", {});
    },

    op_detail_delete(id) {
      let self = this;
      Service.delete(`/app/v1/op/detail/${id}`)
        .then(response => {
          this.bm("Başarıyla silindi");
          let dx;

          self.active.details.forEach((val, index) => {
            if (val.id === id) dx = index;
          });

          if (dx !== undefined) self.active.details.splice(dx, 1);
        })
        .catch(err => {
          this.um("Silinirken bir hata oluştu!" + err);
        });
    },

    op_detail_new_add() {
      let self = this;

      let params = {
        operation: self.active.id,
        field: self.adding.field,
        account: self.adding.account
      };

      if (self.adding.is_debit) params["is_debit"] = self.adding.is_debit;
      if (self.adding.formula) params["formula"] = self.adding.formula;

      Service.post("/app/v1/op/detail", params)
        .then(response => {
          self.bm("Yeni kayıt eklendi.");

          self.$set(self, "adding", {});
          self.active.details.push(response.data);
        })
        .catch(err => {
          self.um("Yeni kayıt eklenirken hata oluştu!" + err);
        });
    },

    reset() {
      this.$set(this, "filter", {});
    }
  }
};
</script>

<style scoped>

</style>
