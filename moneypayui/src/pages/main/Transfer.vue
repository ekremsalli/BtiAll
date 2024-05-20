<template>
  <div class="q-pa-md">
    <div class="q-gutter-md row items-start">
      <q-file
        v-model="file"
        label="Excel dosyası seçiniz"
        filled
        counter
        :counter-label="counterLabelFn"
        style="max-width: 300px"
        accept=".xls, .xlsx"
        :loading="reading"
      >
        <template v-slot:prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>
      <q-btn push color="light-blue-5" label="Dönüştür" size="lg" @click="import_excel" />
    </div>
  </div>
</template>

<script>
import XLSX from 'xlsx'

export default {
  data() {
    return {
      file: null,
      counterLabelFn({ totalSize, filesNumber, maxFiles }) {
        return `${filesNumber} files of ${maxFiles} | ${totalSize}`;
      },
      reading: false,
      excel_records: []
    };
  },
  methods: {
    import_excel() {
      let self = this;

      var reader = new FileReader();
      console.log("importing...", this.file);
      this.$set(this, "reading", true);
      reader.onload = function(e) {
        console.log("file ok!");
        var data = new Uint8Array(e.target.result);
        var workbook = XLSX.read(data, { type: "array" });
        for (const wb in workbook.Sheets) {
            console.log(wb)
          self.$set(
            self,
            "excel_records",
            XLSX.utils.sheet_to_json(workbook.Sheets[wb])
          );
          break;
        }
        self.$set(self, "reading", false);
      };
      reader.readAsArrayBuffer(this.file);
    }
  }
};
</script>
