<script setup lang="ts">
interface Props {
  color?: "white" | "black" | "blue" | "dark-blue";
  width?: "small" | "medium" | "large";
  margin?: "none" | "vertical" | "horizontal";
}

const props = withDefaults(defineProps<Props>(), {
  color: "white",
  margin: "none",
});
</script>

<template>
  <div
    :class="[
      'separator',
      `separator--${props.color}`,
      `separator--${props.width}`,
      `separator--${props.margin}`,
    ]"
  ></div>
</template>

<style lang="scss" src="@/assets/styles/components/atoms/separator.scss" />
