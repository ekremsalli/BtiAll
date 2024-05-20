<template>
    <q-markup-table>
        <thead>
            <tr>
                <th class="text-left">Durum</th>
                <th class="text-left">VT</th>
                <th class="text-left">Oluşturan</th>
                <th class="text-left">Tarih</th>
            </tr>
        </thead>

        <tbody>
            <tr v-for="item in history" :key="item.id">
                <td>
                    <span>
                        {{ item.verify_status }}
                        <q-tooltip>
                            <div style="min-width: 300px">
                                <strong>-Açıklama-</strong> <br />
                                {{ item.description }}


                                <template v-if="item.is_remove_request">
                                    <q-separator class="q-my-sm" inset color="grey" />
                                    Silinme.
                                </template>
                                <template v-else>
                                    <q-separator class="q-my-sm" inset color="grey" />
                                    <strong>-Değişiklik-</strong> <br />
                                    <template v-for="(report, index) in diff(item.snapshot, item.updates)">
                                        <span :key="item.id + '_' + index">
                                            <span class="text-success">
                                                {{ report.key | translate }}
                                            </span> 
                                            >
                                            <span class="text-orange"> {{ report.old }}</span>
                                            >
                                            <span class="text-primary" >{{ report.new }}</span>
                                        </span>
                                    </template>                                    
                                </template>
 
                            </div>
                        </q-tooltip>
                    </span>
    
                </td>
                <td>{{ item.source_db }}</td>
                <td>{{ item.created_by }}</td>
                <td>{{ item.created_on }}</td>
            </tr>
        </tbody>
    </q-markup-table>
</template>

<script>
  import { common } from "src/mixins/common";

  export default {
    mixins: [common],
    props: {
      history: {
        type: Array,
        default () {
            return []            
        }
      }
    },
    methods: {
        diff (s, u) {
            let sx = JSON.parse(s)
            let ux = JSON.parse(u)
            let report = []
            Object.keys(sx).forEach(function(key) {
                if (sx[key] !== ux[key]) {
                    report.push({
                        'key': key,
                        'old': sx[key],
                        'new': ux[key]
                    })
                }
            })

            return report
        }
    }
  }
</script>