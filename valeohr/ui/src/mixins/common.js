import Vue2Filters from "vue2-filters";
import { exportFile } from "quasar";
import currency from "vue2-filters/src/other/currency";

/* eslint-disable */
function wrapCsvValue(val, formatFn) {
  let formatted = formatFn !== void 0 ? formatFn(val) : val;

  formatted =
    formatted === void 0 || formatted === null ? "" : String(formatted);

  formatted = formatted.split('"').join('""');
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`;
}
/* eslint-enable */

const SGUNLER = {
  0: "Pazartesi",
  1: "Salı",
  2: "Çarşamba",
  3: "Perşembe",
  4: "Cuma",
  5: "Cumartesi",
  6: "Pazar"
}

const TRANSLATIONS = {
  'start': 'Başlangıç',
  'end': 'Bitiş'
}

export const common = {
  mixins: [Vue2Filters.mixin],
  created: function() {
    this.$options.gunler = SGUNLER;
  },
  directives: {},
  filters: {
    greeting(name) {
      const day = new Date();
      const hour = day.getHours();
      if (hour >= 5 && hour < 12) {
        return `Günaydın, ${name.trim()}!`;
      } else if (hour >= 12 && hour < 17) {
        return `İyi günler, ${name.trim()}!`;
      } else if (hour >= 17 && hour <= 23) {
        return `İyi akşamlar, ${name.trim()}!`;
      } else {
        return `İyi geceler, ${name.trim()}!`;
      }
    },
    tlira(val) {
      return currency(val, "", 2, {
        decimalSeparator: ",",
        thousandsSeparator: "."
      });
    },
    pretty: function(val) {
      return JSON.stringify(JSON.parse(val), null, 2);
    },
    translate: function(val) {
      if (val in TRANSLATIONS) return TRANSLATIONS[val]
      else return val
    }
  },
  methods: {
    export_2_csv(columns, data, name) {
      // naive encoding to csv format
      /* eslint-disable */
      const content = [columns.map(col => wrapCsvValue(col.label))]
        .concat(
          data.map(row =>
            columns
              .map(col =>
                wrapCsvValue(
                  typeof col.field === "function"
                    ? col.field(row)
                    : row[col.field === void 0 ? col.name : col.field],
                  col.format
                )
              )
              .join(",")
          )
        )
        .join("\r\n");

      const status = exportFile(name + ".csv", content, "text/csv");

      if (status !== true) {
        this.$q.notify({
          message: "Tarayıcı dosya indirme işlemine izin vermedi!...",
          color: "negative",
          icon: "warning"
        });
      }
      /* eslint-enable */
    },
    diff(s, u) {
      let sx = JSON.parse(s);
      let ux = JSON.parse(u);
      let report = [];
      Object.keys(sx).forEach(function(key) {
        if (sx[key] !== ux[key]) {
          report.push({
            key: key,
            old: sx[key],
            new: ux[key]
          });
        }
      });
      return report;
    },
    bm: function(mesaj) {
      const ayarlar = {
        color: "positive",
        position: "top",
        icon: "thumb_up_alt"
      };
      this.um(mesaj, ayarlar);
    },
    um: function(mesaj, ayarlar = {}) {
      const def = {
        color: "negative",
        position: "top",
        icon: "fa fa-exclamation-triangle"
      };
      const param = Object.assign({ message: mesaj }, def, ayarlar);
      this.$q.notify(param);
    },
    filter_fn(val, update, abort, pointer, name, original) {      
      if (val === "") {
        this.$set(this, name, original)
        abort()
      }
      update(() => {
        const needle = val.toLocaleLowerCase()
        if (pointer) 
          this.$set(this, name, original.filter((v) =>
            v[pointer].toLocaleLowerCase().includes(needle)
          ));
        else 
          this.$set(this, name, original.filter((v) =>
            v.toLocaleLowerCase().includes(needle)
          ));        
      });
    } 


  }
};
