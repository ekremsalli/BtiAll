<template>
  <div class="text-center section">
    <Calendar
      class="custom-calendar max-w-full"
      :masks="masks"
      :attributes="attributes"
      :rows='layout.rows'
      :columns='layout.columns'
      :from-date='startDate'
    >
      <template v-slot:day-content="{ day, attributes }">
        <div class="h-full z-10 overflow-hidden">
          <span class="day-label text-sm text-gray-900">{{ day.day }}</span>
          <div class="flex-grow overflow-y-auto overflow-x-auto">
            <p
              v-for="attr in attributes"
              :key="attr.key"
              class="text-xs leading-tight rounded-sm p-6 mt-0 mb-2 etiket"
              :class="attr.customData.class"
            >
              {{ attr.customData.title }}
            </p>
          </div>
        </div>
      </template>
    </Calendar>
  </div>
</template>

<script>
import { Calendar } from 'v-calendar';

const colors = [
  'bg-grey',
  'bg-red',
  'bg-orange',
  'bg-teal',
  'bg-blue',
  'bg-green',
  'bg-pink',
  'bg-purple',
];

export default {
  name: 'FullCalendar',
  props: {
    data: Object,
    year: Number,
  },
  components: {
    Calendar,
  },
  data() {
    return {
      masks: {
        week: 'WWW',
      },
      typesNColors: {},
      attributes: [],
      filteredExcuses: [],
    };
  },
  computed: {
    startDate() {
      return new Date(this.year,0,1);
    },
    layout() {
      return this.$screens(
        {
          // Default layout for mobile
          default: {
            columns: 1,
            rows: 12,
          },
          // Override for large screens
          md: {
            columns: 2,
            rows: 6,
          },
          lg: {
            columns: 3,
            rows: 4,
          },
        },
      );
    },
  },
  mounted(){
    this.setFilteredExcuses();
    this.setAttributes();
  },
  watch: {
    data(){
      this.setFilteredExcuses();
      this.setAttributes();
    }
  },
  methods: {
    getColor(type) {
      if (!this.typesNColors[type]) {
        this.typesNColors[type] = colors[Math.floor(Math.random() * colors.length)];
      }
      return this.typesNColors[type];
    },
    setFilteredExcuses(){
            /* eslint-disable */
      this.filteredExcuses = this.data?.cur_data?.length === 0 ? [] : this.data.cur_data.map(({ tr_date, excuse }) => ({
        date: new Date(tr_date),
        type: excuse,
      }));
    },
    setAttributes(){
      let key = 0;
      this.attributes = this.filteredExcuses.map((d) => {
        key += 1;
        return {
          key,
          customData: {
            title: d.type,
            class: `${this.getColor(d.type)} text-white`,
          },
          dates: d.date,
        };
      });
    }
  },
};
</script>

<style lang="scss" scoped>
::-webkit-scrollbar {
  width: 0px;
}

::-webkit-scrollbar-track {
  display: none;
}

::v-deep .custom-calendar.vc-container {
  --day-border: 1px solid #b8c2cc;
  --day-border-highlight: 1px solid #b8c2cc;
  --day-width: 50px;
  --day-height: 50px;
  --weekday-bg: #f8fafc;
  --weekday-border: 1px solid #eaeaea;

  border-radius: 0;
  width: 100%;

  & .vc-header {
    background-color: #f1f5f8;
    padding: 10px 0;
  }
  & .vc-weeks {
    padding: 0;
    border: .5px dotted rgba(56, 56, 56, 0.829);
  }
  & .vc-weekday {
    background-color: var(--weekday-bg);
    border-bottom: var(--weekday-border);
    border-top: var(--weekday-border);
    padding: 5px 0;
  }
  & .vc-day {
    padding: 0 5px 3px 5px;
    text-align: left;
    height: var(--day-height);
    min-width: var(--day-width);
    background-color: white;
    &.weekday-1,
    &.weekday-7 {
      background-color: #eff8ff;
    }
    &:not(.on-bottom) {
      border-bottom: var(--day-border);
      &.weekday-1 {
        border-bottom: var(--day-border-highlight);
      }
    }
    &:not(.on-right) {
      border-right: var(--day-border);
    }
  }
  & .vc-day-dots {
    margin-bottom: 5px;
  }
  .etiket{
    padding: .3px 2px;
    border-radius: 4px;
    text-align: center;
    font-weight: 600;
  }
  .on-right, .on-left{
    margin: 0px !important;
  }
  .vc-arrow{
    display: none;
  }
}
</style>
