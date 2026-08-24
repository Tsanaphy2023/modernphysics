/** Precision Instrument Console routes: geometry workbench plus the Nano Materials instrument hub. */
import { Toaster } from "@/components/ui/sonner";
import { TooltipProvider } from "@/components/ui/tooltip";
import NotFound from "@/pages/NotFound";
import { Route, Switch } from "wouter";
import ErrorBoundary from "./components/ErrorBoundary";
import { ThemeProvider } from "./contexts/ThemeContext";
import Home from "./pages/Home";
import NanoMaterials from "./pages/NanoMaterials";
import QuantumMaterials from "./pages/QuantumMaterials";
import StmSts from "./pages/StmSts";

function Router() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route path="/materials" component={NanoMaterials} />
      <Route path="/quantum-materials" component={QuantumMaterials} />
      <Route path="/stm-sts" component={StmSts} />
      <Route path="/404" component={NotFound} />
      <Route component={NotFound} />
    </Switch>
  );
}

function App() {
  return (
    <ErrorBoundary>
      <ThemeProvider defaultTheme="dark">
        <TooltipProvider>
          <Toaster richColors position="top-center" />
          <Router />
        </TooltipProvider>
      </ThemeProvider>
    </ErrorBoundary>
  );
}

export default App;
