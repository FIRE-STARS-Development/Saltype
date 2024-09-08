<script setup lang="ts">
interface Props {
  imageSrc: string;
  alt?: string;
  width?: "mini" | "small" | "medium" | "large";
  height?: "mini" | "small" | "medium" | "large";
}

const props = withDefaults(defineProps<Props>(), {
  width: "medium",
  height: "medium",
});
</script>

<template>
  <img
    :src="`${props.imageSrc}`"
    :alt="`${props.alt}`"
    :class="[`img-width--${props.width}`, `img-height--${props.height}`]"
  />
</template>

<style lang="scss" src="@/assets/styles/components/atoms/image.scss" />
