/** @odoo-module **/

import { onMounted, onWillUnmount } from "@odoo/owl";

export function useInterval(func, ms) {
  let intervalId;

  onMounted(() => {
    intervalId = setInterval(func, ms);
  });

  onWillUnmount(() => {
    clearInterval(intervalId);
  });
}
