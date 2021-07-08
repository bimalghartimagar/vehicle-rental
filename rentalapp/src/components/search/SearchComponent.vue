<template>
  <div>
  <div class="text-center text-h5">
    {{data.length}} results found
    </div>
    <div class="d-flex flex-wrap justify-space-around w-4">
      <SearchItem
        v-for="item in data"
        :key="item.id"
        :item="item"
        class="align-content-space-around mb-8"
      />
    </div>
  </div>
</template>

<script>
import SearchItem from "@/components/search/SearchItem";
export default {
  components: {
    SearchItem,
  },

  props: {
    data: {
      type: Array,
      required: true,
    },
    queryParams: {
      type: Object,
      required: true,
    },
  },
};
</script>
