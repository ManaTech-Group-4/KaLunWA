import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import {MatMenuModule} from '@angular/material/menu';
import { MatIconModule } from '@angular/material/icon';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatCardModule} from '@angular/material/card';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatPaginatorModule, PageEvent} from '@angular/material/paginator';
import {MatChipsModule} from '@angular/material/chips';
const MATERIAL = [
  MatToolbarModule,
  MatButtonModule,
  MatMenuModule,
  MatIconModule,
  MatSidenavModule,
  MatCardModule,
  MatButtonToggleModule,
  MatPaginatorModule,
  MatChipsModule
];

@NgModule({
  declarations: [],
  exports: [MATERIAL],
  imports: [
    CommonModule,
    MATERIAL
  ]
})
export class MatDesignModule { }
