import { Directive, ElementRef, HostListener, NgModule } from '@angular/core';

@Directive({
  selector: '[appPrev]'
})
export class PrevDirective {

  constructor(private el:ElementRef) { }

  @HostListener('click')
  prevFunc(){
    var elm = this.el.nativeElement.parentElement.parentElement.children[0];
    var item = elm.getElementsByClassName("item");
    elm.prepend(item[item.length-1]);
  }

}

@NgModule({
  declarations: [ PrevDirective ],
  exports: [ PrevDirective ]
})

export class PrevDirectiveModule {}